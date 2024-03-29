import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load the left and right images in grayscale
imgL = cv.imread('tsukuba_l.png', cv.IMREAD_GRAYSCALE)
imgR = cv.imread('tsukuba_r.png', cv.IMREAD_GRAYSCALE)

# Create a StereoBM object
stereo = cv.StereoBM.create(numDisparities=16, blockSize=15)

# Compute the disparity map
disparity = stereo.compute(imgL, imgR)

# Display the disparity map
plt.imshow(disparity, 'gray')
plt.show()