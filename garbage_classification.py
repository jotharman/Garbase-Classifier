import keras
import flask
from tensorflow.keras.preprocessing import image
import numpy as np

MODEL_ADDRESS = "./classification_model"
model = keras.models.load_model(MODEL_ADDRESS)


app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route("/")
def predict():
    img_path = flask.request.args['add']
    img = image.load_img(img_path, target_size=(224, 224, 3))
    print("\n\n\n\n\n\n\n\n\n\n\n\n {} \n\n\n\n\n\n\n\n\n\n\n\n", img)
    img_array = image.img_to_array(img)
    img_array = img_array.reshape((1, 224, 224, 3))
    print("IMG_SHAPE", img_array.shape)
    result = np.argmax(model.predict(img_array))
    print("\n\n\n\nRESULT::: ", result)
    return str(result)

app.run() 