# OCR Image Scanner
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is an OCR image scanner built as a Flask web app using OpenCV for image processing and tesseract for image recognition. It allows the user to upload an image, which is first processed so that text in the image is easier to recognize and differentiate from its background. This processed image is then passed onto tesseract which performs image recognition and outputs the text in this image.
## Features
Image processing ensures that the text in that image is readable. It does so by first converting the image to grayscale and thresholding the image. An additional feature that the image processing script performs is deskewing text in this image so that tesseract's image recognition works efficiently.
## Limitations
Tesseract has its own set of limitations. It fails to deliver when passed images of different fonts or when font sizes are too small. Though image processing eliminates the noise in images to an extent, extremely noisy images don't do well with tesseract. This app may not do well with bordered images either.
## Usage
### Prerequisites
##### Independant installations:
* `python 3.5`
* `leptonica`
* `tesseract`
##### Python packages:
* `flask`
* `pytesseract`
* `Pillow`
* `OpenCV`

__Note:__ [CONTRIBUTING.md](https://github.com/utkarsh23/OCR-Image-Scanner/blob/master/CONTRIBUTING.md) contains detailed instructions on setting up the prerequisites.
### Running the Flask app
Execute the following after cloning this repository:
``` bash
export FLASK_APP=app.py
flask run
```
## Contributing
[CONTRIBUTING.md](https://github.com/utkarsh23/OCR-Image-Scanner/blob/master/CONTRIBUTING.md) contains detailed instructions on how to contribute to this repository.
