import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/surya/PycharmProjects/pythonProject/thalapathy.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((5,5), np.uint8)

# Apply closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Show the results
cv2.imshow('Input Image', img)
cv2.imshow('Closed Image', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
