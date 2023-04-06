# -*- coding: utf-8 -*-
"""threshold.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i4yb51BryBwipsWJqsKyLmAMQX6dwaRO
"""



import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_minimum
from skimage.filters import threshold_mean
from skimage.filters import threshold_otsu

image = data.camera()
treshmin =threshold_minimum(image)
print("Treshold minimum: ", treshmin)
minimumImage = image > treshmin

treshmean =threshold_mean(image)
print("Treshold mean: ", treshmean)
meanImage = image > treshmean


fig, axes = plt.subplots(3,2, figsize=(10,10))
ax = axes.ravel()
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title("original")
ax[1].hist(image.ravel(), bins=256)
ax[1].set_title("Histogram image")

ax[2].imshow(minimumImage, cmap=plt.cm.gray)
ax[2].set_title("Treshold minimum")
ax[3].hist(image.ravel(), bins=256)
ax[3].set_title("Histogram minimum")


ax[4].imshow(meanImage, cmap=plt.cm.gray)
ax[4].set_title("Treshold mean")
ax[5].hist(image.ravel(), bins=256)
ax[5].set_title("Histogram mean")

plt.tight_layout()