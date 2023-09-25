#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU

import matplotlib.pyplot as plt
import numpy as np

damenik = int(input("Enter the Size:"))
output = input("Enter output file:")

img = np.ones((damenik,damenik,3))

img[::2,:,1] = 0
img[::2,:,2] = 0

plt.imsave(output,img)