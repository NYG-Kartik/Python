# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/7/23
# This program prints the shape 6 in blue on a yellow background
import matplotlib.pyplot as plt
import numpy as np
x = input('Enter output file name: ')
img = np.ones((30,30,3))
img[:,:,0] = 1
img[:,:,1] = 1
img[:,:,2] = 0
img[3:26, 4:7, :] = [0,0,1]
img[13:16, 4:26, :] = [0,0,1]
img[24:27, 4:26, :] = [0,0,1]
img[15:27, 23:26, :] = [0,0,1]
plt.imsave(x, img)



