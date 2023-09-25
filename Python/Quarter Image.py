#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.Edu


import matplotlib.pyplot as plt
import numpy as np

image = input("Enter an image file name: ")
output = input("Enter output file: ")

image = plt.imread(image)

height = image.shape[0]
width = image.shape[1]

image2 = image[height//2:, :width//2]

plt.imsave(output, image2)