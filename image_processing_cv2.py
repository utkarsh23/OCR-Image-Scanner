import cv2
import time
import numpy as np

def image_processing(file, dest):
	# read the image
	image = cv2.imread(file)

	# convert image to grayscale and make foreground white and background black
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.bitwise_not(gray)
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# coordinates of pixels greater than background (0px) are passed to minAreaRect
	# minAreaRect computes the minimum rotated rectangle that contains the entire text region
	coords = np.column_stack(np.where(thresh > 0))
	angle = cv2.minAreaRect(coords)[-1]
	if angle < -45:
		angle = -(90 + angle)
	else:
		angle = -angle

	# deskew the grayscale image
	(h, w) = gray.shape[:2]
	center = (w // 2, h // 2)
	M = cv2.getRotationMatrix2D(center, angle, 1.0)
	rotated = cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

	# saving the processed image
	cv2.imwrite(dest, rotated)