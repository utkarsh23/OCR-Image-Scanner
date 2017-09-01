# Contribution Guidelines
## Setting up the prerequisites
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
### Installing independant packages
##### Installing leptonica and tesseract from source
* [Tesseract's wiki page on compililing](https://github.com/tesseract-ocr/tesseract/wiki/Compiling) contains instructions on how to build `leptonica` and `tesseract` from source.
* [Video representation of the compiling process](https://github.com/tesseract-ocr/tesseract/wiki/Compiling#video-representation-of-the-compiling-process-for-tesseract-40-and-leptonica-174-on-ubuntu-16xx) is very much recommended as the videos contain stepwise explanation on building from source.
##### Installing python 3.5
``` bash
sudo apt-get update
sudo apt-get install python3.5
```
### Setting up virtual environment
##### Conda installation
Conda is a package, dependency and environment manager. We can use this to set up our environment and run out web app. [Conda installation docs](https://conda.io/docs/user-guide/install/index.html) contain instructions on how to setup conda.
##### Create virtual environment
Creating a new environment and activating it:
``` bash
conda create -n envname python=3.5
source activate envname
```
Deactivating the environment:
``` bash
source deactivate
```
### Installing python packages
``` bash
conda install -c anaconda flask
conda install -c auto pytesseract 
conda install -c anaconda pillow 
conda install -c menpo opencv3 
```
## Running the Flask app
Execute the following after cloning this repository and setting up the above prerequisites:
``` bash
export FLASK_APP=app.py
flask run
```
## Contributing
* Fork this repository
* Make changes locally and push them onto your forked repository
* Create a pull request with all changes and commits into this repository
