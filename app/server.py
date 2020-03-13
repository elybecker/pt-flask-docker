import flask
from PIL import Image
import io, logging
from prediction import inference
from flask import Flask, request, jsonify
#from flask_restful import Resource, Api
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
#api = Api(app)

@app.route("/", methods=["GET"])
def home():
    return "Hello World!"

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    if flask.request.files.get("image"):
        logger.info('Reading image')    
        image = flask.request.files["image"].read()
        image = Image.open(io.BytesIO(image))

        logger.info('Prefroming Prediction') 
        result = inference(image)

        data["response"] = result
        data["success"] = True
        print(data)
    return flask.jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)