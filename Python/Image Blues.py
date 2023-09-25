#DAMENIK THAQI
#DAMENIK.THAQI50@MYHUNTER.CUNY.EDU


import matplotlib.pyplot as plt
import numpy as np

loadfile = input("Enter name of input file: ") 
savefile = input("Enter name of output file: ")

img = plt.imread(loadfile)   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy() 
#make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0
img2[:,:,0] = 0   #Set the blue channel to 0


plt.imsave(savefile, img2)  #Save the image we created to the file: reds.pn