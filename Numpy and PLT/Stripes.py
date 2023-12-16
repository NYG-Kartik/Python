# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/8/23
# This program prints purple and yellow stripes every 
# other line no matter the size of the image.

import matplotlib.pyplot as plt
import numpy as np

x = int(input('Enter the size:'))
y = input('Enter output file:')

img = np.ones((x,x,3))
img[:,:,0:2] = 1
img[:,:,2] = 0
img[::2,:,1] = 0
img[::2,:,0] = 1
img[::2,:,2] = 1

plt.imsave(y, img)
