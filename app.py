try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract
import os
from flask import Flask, render_template, request
from image_processing_cv2 import image_processing

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
	target = os.path.join(APP_ROOT, 'static/images/')

	if not os.path.isdir(target):
		os.mkdir(target)

	file = request.files.getlist("file")[0]
	filename = file.filename
	destination = "".join([target, filename])
	file.save(destination)

	imagepath = "./static/images/" + filename
	save_to_file = filename.split(".")
	save_to_file = "./static/images/" + save_to_file[0] + "_optimized." + save_to_file[1]
	image_processing(imagepath, save_to_file)

	text = pytesseract.image_to_string(Image.open(save_to_file))

	return render_template("complete.html", image_unprocessed=imagepath, image_processed=save_to_file, display=text)

if __name__ == "__main__":
	app.run(debug=True)