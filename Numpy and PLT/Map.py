# Kartik Vanjani
# KARTIK.VANJANI21@myhunter.cuny.edu
# 3/10/23
# This program prints a flood map
import numpy as np
import matplotlib.pyplot as plt



elevations = np.loadtxt('elevationsNYC.txt')


mapShape = elevations.shape + (3,)


floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            
           floodMap[row,col,2] = 1.0     
        elif elevations[row,col] <= 6:
            
           floodMap[row,col,0] = 1.0
           floodMap[row,col,1] = 128/255
           floodMap[row,col,2] = 0
        elif 6 < elevations[row,col] <= 13:
           floodMap[row,col,0] = 0.25
           floodMap[row,col,1] = 0.25
           floodMap[row,col,2] = 0.25
        elif 13 < elevations[row,col] <= 20:
           floodMap[row,col,0] = 0.75
           floodMap[row,col,1] = 0.75
           floodMap[row,col,2] = 0.75
        elif elevations[row,col] >= 20:
           floodMap[row,col,1] = 1.0
        else:
            
            floodMap[row,col,1] = 1.0   



plt.imsave('floodMap.png', floodMap)
