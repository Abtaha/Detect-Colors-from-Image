# import the necessary packages
import numpy as np
import argparse
import cv2


try:
	img = input("Enter your image >> ")
	image = cv2.imread(img)
except:
	print("Error, exitting")


lower = np.array([0, 0, 0])

upper = np.array([60, 60, 255])
mask = cv2.inRange(image, lower, upper)
red = cv2.bitwise_and(image, image, mask = mask)

upper = np.array([60, 255, 60])
mask = cv2.inRange(image, lower, upper)
green = cv2.bitwise_and(image, image, mask = mask)

upper = np.array([255, 60, 60])
mask = cv2.inRange(image, lower, upper)
blue = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow("red", red)
cv2.imshow("green", green)
cv2.imshow("blue", blue)

cv2.waitKey(0)
cv2.destroyAllWindows()