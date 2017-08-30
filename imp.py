import cv2
import time

def image_processing(file):
	image = cv2.imread(file)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	cv2.imwrite(file, gray)
	time.sleep(10)