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
	return "Thanks for your contribution, we will contact you."
	

@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html')

@app.route("/predict", methods=['POST'])
def predict():
	MODEL_ADDRESS = "./classification_model"
	model = keras.models.load_model(MODEL_ADDRESS)


	# MASK_MODEL_ADDRESS = "./VGG19-facemask"
	# mask_model = keras.models.load_model(MASK_MODEL_ADDRESS)

	file =  request.files['file']
	filename = file.filename
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	path = os.getcwd()
	img_path = str(path)+'/static/uploads/'+ filename


	img = image.load_img(img_path, target_size=(224, 224, 3))
	# mask_img = image.load_img(img_path, target_size=(160, 160, 3))
	print("\n\n\n\n\n\n\n\n\n\n\n\n {} \n\n\n\n\n\n\n\n\n\n\n\n", img)
	img_array = image.img_to_array(img)
	# img_arr = image.img_to_array(mask_img)
	img_array = img_array.reshape((1, 224, 224, 3))
	# img_arr = img_arr.reshape((1, 160, 160, 3))
	print("IMG_SHAPE", img_array.shape)
	# mask_result = np.argmax(mask_model.predict(img_arr)) 
	# if str(mask_result) == '0':
	result = np.argmax(model.predict(img_array))
	if str(result) == '1':
		return "The uploaded is that of cardboard"
		# return "The given image is that of mask, you can fill the details in the side box for selling the waste masks!"
	elif str(result) == '2':
		return "The uploaded is that of Glass"
	elif str(result) == '3':
		return "The uploaded is that of Metal"
	elif str(result) == '4':
		return "The uploaded is that of Paper"
	elif str(result) == '5':
		# return "The uploaded is that of Plastic"
		return "The given image is that of mask, you can fill the details in the side box for selling the waste masks!"
	elif str(result) == '6':
		return "The uploaded is that of Trash"
		# elif str(result) == '6':
		# 	return "The uploaded is that of cardboard"

	# elif str(mask_result) == '1':
	# 	return "The given image is that of mask, you can fill the details in the side box for selling the waste masks!"


    


if __name__ == "__main__":
   app.run(debug=True)

