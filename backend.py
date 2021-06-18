from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from flask import Flask, render_template, request
import keras
import flask
from tensorflow.keras.preprocessing import image
import numpy as np
import PIL
import os



app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_PATH']

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

MODEL_ADDRESS = "./classification_model"
model = keras.models.load_model(MODEL_ADDRESS)

serviceUsername = "apikey-v2-1a60ckzysfp6feh01ims6rkmq2jod3yo513u4wijsbzl"
servicePassword = "a134014e50ce02db60dba2423a457fd5"
serviceURL = "https://apikey-v2-1a60ckzysfp6feh01ims6rkmq2jod3yo513u4wijsbzl:a134014e50ce02db60dba2423a457fd5@6d0320e9-1f78-4a29-a55a-ef2b2f231ea0-bluemix.cloudantnosqldb.appdomain.cloud"
# API_KEY = "TFYiVrpV7If2nTqIkG6KXak-1wEw_cFQMIGv9Qz7iQ3p"
# ACCOUNT_NAME = "Service credentials-1"
# client = Cloudant.iam(ACCOUNT_NAME, API_KEY, connect=True)


client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = "databasewit"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))



@app.route('/')
def index():
	# coverpic = url('CoverPic.jpg')
	return render_template('Home.html')

@app.route('/waste_coll')
def waste_coll():
	return render_template('Teams.html')

@app.route('/data', methods=['POST'])
def data_entry():
	Full_name = request.form.get("Name")
	Email_add = request.form.get("email")
	Phone_number = request.form.get("Phone number")
	jsonDocument = {
	"Name": Full_name,
	"Email": Email_add,
	"Phone_number": Phone_number
	}
	newDocument = myDatabaseDemo.create_document(jsonDocument)
	if newDocument.exists():
		print("Document '{0}' successfully created.".format(Full_name))
	print(Full_name)
	print("NICEEEEEEEEEEEEEEEEEEE")
	return "nice"
	

@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html')

@app.route("/predict", methods=['POST'])
def predict():
	# filename = request.form.get("img")
	file =  request.files['file']
	filename = file.filename
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	# img_path = os.path+filename
	img_path = os.path.abspath(filename)
	print(img_path)
	img = image.load_img(img_path, target_size=(224, 224, 3))
	print("\n\n\n\n\n\n\n\n\n\n\n\n {} \n\n\n\n\n\n\n\n\n\n\n\n", img)
	img_array = image.img_to_array(img)
	img_array = img_array.reshape((1, 224, 224, 3))
	print("IMG_SHAPE", img_array.shape)
	result = np.argmax(model.predict(img_array))
	print("\n\n\n\nRESULT::: ", result)
	return str(result)
    # img_path = flask.request.args['add']
    


if __name__ == "__main__":
   app.run(debug=True)

