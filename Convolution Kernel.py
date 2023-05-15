import cv2
import numpy as np

# Load the input image in grayscale
img = cv2.imread('C:/Users/surya/PycharmProjects/pythonProject/thalapathy.jpg', cv2.IMREAD_GRAYSCALE)

# Compute the Sobel gradients in the x and y directions
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude of the gradients
mag = cv2.magnitude(dx, dy)

# Threshold the magnitude image to create a binary image
thresh = 50
mag[mag < thresh] = 0
mag[mag >= thresh] = 255

# Save the resulting image
cv2.imwrite('boundary.jpg', mag)
