import numpy as np
import matplotlib.pyplot as plt

img = np.ones((10,10,3))

img[0:8,5:] = 0
plt.imshow(img)
plt.show()