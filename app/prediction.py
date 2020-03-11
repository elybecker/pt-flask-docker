import os
import json, time, logging, torch
import torch.nn.functional as F
from torchvision import transforms

logger = logging.getLogger()
logger.setLevel(logging.INFO)


"""Returns model loaded from disc"""
def load_model():
    model_dir = 'model'
    classes = open(os.join([model_dir,'classes']),'r').read().splitlines()
    logger.info('Classes are {}'.format(classes))    

    model_path = os.join([model_dir,'simplecifar_jit.pth'])
    logger.info('Model path is {}'.format(model_path))  

    use_cuda = torch.cuda.is_available()
    device = torch.device('cuda' if use_cuda else 'cpu')
    
    model = torch.jit.load(model_path, map_location=device)
    logger.info('Deploying model to device: {}'.format(device)) 
    return model.eval(), classes

"""Resturns the final prediction and it's correponding probability given an image"""
def prediction(model, classes, image_tensor):
    predict_values = model(image_tensor)
    softmax_dist = F.softmax(predict_values, dim=1)
    probability_tensor, index = torch.max(softmax_dist, dim=1)

    prediction = classes[index]
    probability = "{:1.2f}".format(probability_tensor.item())

    logger.info('Predicted class is {} with a probability of {}'.format(prediction, probability)) 
    return {'class': prediction, 'probability': probability}

 """Transforms the posted image to a PyTorch Tensor."""
def image_to_tensor(img):

    img_tensor = preprocess_pipeline(img)
    img_tensor = img_tensor.unsqueeze(0).cuda() # 3d to 4d for batch
    return img_tensor

"""The main inference function which gets passed an image to classify"""
def inference(img):
    

    image_tensor = image_to_tensor(img)
    response = predict(model, classes, image_tensor)
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }


model, classes = load_model()

preprocess_pipeline = transforms.Compose([
    transforms.Resize(50),
    transforms.CenterCrop(32),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])