# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/2/23
# This program prints Hunter Bridge in purple
import matplotlib.pyplot as plt
import numpy as np
x = input("Enter name of the input file:")
y = input("Enter name of the output file:")
img = plt.imread(x)
img2 = img.copy()
img2[:,:,1] = 0

plt.imsave(y, img2)