import matplotlib.pyplot as plt
import math
import random
from scipy.stats import entropy
from skimage.io import imread, imsave
from skimage.measure import shannon_entropy
import numpy as np
image = imread("image1.jpeg")
#image = imread("image1.bmp")
#image = imread("image1.tiff")
#image = imread("image1.png")
#image = imread("/home/kali/Desktop/TI/Data/image2.jpeg")
#image = imread("/home/kali/Desktop/TI/Data/image3.jpeg")

#fig = plt.figure()

#new_type = imsave("image1.bmp", arr=image)
#new_type = imsave("image1.tiff", arr=image)
#new_type = imsave("image1.png", arr=image)
#new_type = imsave("image1.jpeg", arr=image)

#plt.axis('off')
#plt.show()
#h = [(image == i).sum() for i in range(256)]
#plt.bar(range(256), h)
#plt.show()

def my_image_entropy(image):
    pixel_probs = np.histogramdd(np.ravel(image), bins=256)[0] / image.size
    pixel_probs = list(filter(lambda p: p > 0, np.ravel(pixel_probs)))
    entropy = -np.sum(np.multiply(pixel_probs, np.log2(pixel_probs)))
    return entropy


print("My entropy", my_image_entropy(image))
print("Correct entropy", shannon_entropy(image, base=2))

