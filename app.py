try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract
import os
from flask import Flask, render_template, request
from imp import image_processing

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
	target = os.path.join(APP_ROOT, 'static/')
	print(target)

	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist("file"):
		print(file)
		filename = file.filename
		destination = "".join([target, filename])
		print(destination)
		file.save(destination)
		imagepath = "./static/" + filename
		image_processing(imagepath)

	text = pytesseract.image_to_string(Image.open(imagepath))

	return render_template("complete.html", display=text, image=imagepath)

if __name__ == "__main__":
	app.run(debug=True)