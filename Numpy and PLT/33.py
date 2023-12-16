# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/29/23
# This program prints the top left of an image or middle based on the user choice

# import libraries to work with images and the plot for cropping
import matplotlib.pyplot as plt
import numpy as np

# choices
print('Enter 1 to get top left corner')
print('Enter 2 to get middle portion')
choice = input('Your choice:')

if choice not in["1", "2"]:
    print('wrong choice')
    exit()

image = input('Enter input file name:')
image2 = input('Enter output file name:')
img = plt.imread(image)
height = img.shape[0]
width = img.shape[1]


if choice == "1":
    img2 = img[:height//2, :width//2]
elif choice == "2":
    img2 = img[height//4:3*(height)//4, width//4:3*(width)//4]

 
plt.gcf()
plt.imsave(image2, img2)
    
