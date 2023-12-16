# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/13/23
# This program prints a complement of an image.
import matplotlib.pyplot as plt
import numpy as np
x = input('Enter file name:')
y = float(input('Enter threshold:'))

ca = plt.imread(x)   
height = ca.shape[0]
width = ca.shape[1]
countSnow = 0   
z = ca.copy()         
t = y               

#For every pixel:
for i in range(height):
     for j in range(width):
          #Check if red, green, and blue are < t:
          if (ca[i,j,0] < t) and (ca[i,j,1] < t) and (ca[i,j,2] < t):
               countSnow = countSnow + 1
percent = countSnow / (i*j) * 100
print('number of pixels whose rgb are small than threshold in original figure:', countSnow)
print('percent of those pixels:', round(percent,2), '%')
z[i,j,0] = 1 - ca[i,j,0]
z[i,j,1] = 1 - ca[i,j,1]
z[i,j,2] = 1 - ca[i,j,2]
percent = countSnow / (i*j) * 100
print('number of pixels whose rgb are small than threshold in original figure:', countSnow)
print('percent of those pixels:', round(percent,2), '%')
name = x.split('.')
plt.imsave(name, z)