#DAMENIK THAQI
#DAMENIK.THAQI50@myhunter.cuny.edu

import matplotlib.pyplot as plt
import numpy as np

fileName = input('Enter file name: ')
threshold = 0.75

img = plt.imread(fileName)

count = 0
countPixel = 0

for i in range(img.shape[0]): # accessing rows
    for q in range(img.shape[1]): # accessing columns
        countPixel+=1


for i in range(img.shape[0]): # accessing rows
    for a in range(img.shape[1]): # accessing columns
        if (img[i, a, 0] > threshold) and (img[i, a, 1] > threshold) and (img[i, a, 2] > threshold): # if any of the color channels, r g b are < threshold. Each pixel is accessed & checked with the for loop [row,col, all color channels].
            count+=1 # we count up by one

print('Number of pixels whose rgb are smaller than threshold in original figure: ', count)
print('Percent of those pixels: ', (count/countPixel)*100, '%')