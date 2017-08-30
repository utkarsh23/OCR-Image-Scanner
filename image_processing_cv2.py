import cv2
import time

def image_processing(file, dest):
	image = cv2.imread(file)
	gray = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converts color image to greyscale
	gray = cv2.bitwise_not(gray)
	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] #darkens black text
	cv2.imwrite(dest, gray)