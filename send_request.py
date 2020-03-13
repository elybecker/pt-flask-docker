import requests
import sys

# PORT outside the docker container
API_URL = 'http://0.0.0.0:7777/predict'

def predict_result(image_path):
    image = open(image_path, 'rb').read()
    payload = {'image': image}
    print("Sending request for {}".format(img_path))
    r = requests.post(API_URL, files=payload).json()

    return r

img_path = sys.argv[1]
print("Checking results for {}".format(img_path))
result = predict_result(img_path)
print(result)