import matplotlib.pyplot as plt
import cv2
import numpy as np

five = cv2.imread("5.png")

# acces pixel of images per postion
pixels = five[100,100]
print(pixels)
