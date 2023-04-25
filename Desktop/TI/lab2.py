import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.stats import entropy
from PIL import Image, ImageOps
from skimage.measure import shannon_entropy
from scipy.special import rel_entr, kl_div

img = Image.open('lab2image.png')

gray = ImageOps.grayscale(img)
#gray.save("gray.png")

#print("Entropy of gray image =", end=" ")
#print(shannon_entropy(gray))

resized_img2 = gray.resize((round(gray.size[0] * 0.5), round(gray.size[1] * 0.5)), Image.ANTIALIAS)
#resized_img2.save("resized_img2.png")

resized_img4 = gray.resize((round(gray.size[0] * 0.25), round(gray.size[1] * 0.25)), Image.ANTIALIAS)
#resized_img4.save("resized_img4.png")

q_img_8 = img.quantize(colors=8)
#q_img_8.save("q_img_8.png")

q_img_16 = img.quantize(colors=16)
#q_img_16.save("q_img_16.png")

q_img_64 = img.quantize(colors=64)
#q_img_64.save("q_img_64.png")

q_resized_img2_8 = resized_img2.quantize(colors=8)
#q_resized_img2_8.save("q_resized_img2_8.png")

q_resized_img2_16 = resized_img2.quantize(colors=16)
#q_resized_img2_16.save("q_resized_img2_16.png")

q_resized_img2_64 = resized_img2.quantize(colors=64)
#q_resized_img2_64.save("q_resized_img2_64.png")

q_resized_img4_8 = resized_img4.quantize(colors=8)
#q_resized_img4_8.save("q_resized_img4_8.png")

q_resized_img4_16 = resized_img4.quantize(colors=16)
#q_resized_img4_16.save("q_resized_img4_16.png")

q_resized_img4_64 = resized_img4.quantize(colors=64)
#q_resized_img4_64.save("q_resized_img4_64.png")

#print("Entropy of gray image with discret step 2 =", end=" ")
#print(shannon_entropy(resized_img2))

#print("Entropy of gray image with discret step 4 =", end=" ")
#print(shannon_entropy(resized_img4))

#print("Entropy of start image with quantize level 8 =", end=" ")
#print(shannon_entropy(q_img_8))

#print("Entropy of start image with quantize level 16 =", end=" ")
#print(shannon_entropy(q_img_16))

#print("Entropy of start image with quantize level 64 =", end=" ")
#print(shannon_entropy(q_img_64))

#print("Entropy of gray image with discret step 2 and quantize level 8 =", end=" ")
#print(shannon_entropy(q_resized_img2_8))

#print("Entropy of gray image with discret step 2 and quantize level 16 =", end=" ")
#print(shannon_entropy(q_resized_img2_16))

#print("Entropy of gray image with discret step 2 and quantize level 64 =", end=" ")
#print(shannon_entropy(q_resized_img2_64))

#print("Entropy of gray image with discret step 4 and quantize level 8 =", end=" ")
#print(shannon_entropy(q_resized_img4_8))

#print("Entropy of gray image with discret step 4 and quantize level 16 =", end=" ")
#print(shannon_entropy(q_resized_img4_16))

#print("Entropy of gray image with discret step 4 and quantize level 64 =", end=" ")
#print(shannon_entropy(q_resized_img4_64))

restored_img2_nearest = resized_img2.resize((round(resized_img2.size[0] * 2), round(resized_img2.size[1] * 2)), Image.NEAREST)
#restored_img2_nearest.save("restored_img2_nearest.png")

restored_img2_bilinear = resized_img2.resize((round(resized_img2.size[0] * 2), round(resized_img2.size[1] * 2)), Image.BILINEAR)
#restored_img2_bilinear.save("restored_img2_bilinear.png")

restored_img2_bicubic = resized_img2.resize((round(resized_img2.size[0] * 2), round(resized_img2.size[1] * 2)), Image.BICUBIC)
#restored_img2_bicubic.save("restored_img2_bicubic.png")

restored_img4_nearest = resized_img4.resize((round(resized_img4.size[0] * 4), round(resized_img4.size[1] * 4)), Image.NEAREST)
#restored_img4_nearest.save("restored_img4_nearest.png")

restored_img4_bilinear = resized_img4.resize((round(resized_img4.size[0] * 4), round(resized_img4.size[1] * 4)), Image.BILINEAR)
#restored_img4_bilinear.save("restored_img4_bilinear.png")

restored_img4_bicubic = resized_img4.resize((round(resized_img4.size[0] * 4), round(resized_img4.size[1] * 4)), Image.BICUBIC)
#restored_img4_bicubic.save("restored_img4_bicubic.png")

#print("Entropy of restored image with discret step 2 with nearest neighbour method =", end=" ")
#print(shannon_entropy(restored_img2_nearest))

#print("Entropy of restored image with discret step 2 with bilinear method =", end=" ")
#print(shannon_entropy(restored_img2_bilinear))

#print("Entropy of restored image with discret step 2 with bicubic method =", end=" ")
#print(shannon_entropy(restored_img2_bicubic))

#print("Entropy of restored image with discret step 4 with nearest neighbour method =", end=" ")
#print(shannon_entropy(restored_img4_nearest))

#print("Entropy of restored image with discret step 4 with bilinear method =", end=" ")
#print(shannon_entropy(restored_img4_bilinear))

#print("Entropy of restored image with discret step 4 with bicubic method =", end=" ")
#print(shannon_entropy(restored_img4_bicubic))

def img_relative_entropy(pk, qk):
    #return kl_div(pk, qk)
    hist1, _ = np.histogram(pk, bins=256, range=(0, 255))
    hist2, _ = np.histogram(qk, bins=256, range=(0, 255))
    
    p = hist1.astype(float) / np.sum(hist1)
    q = hist2.astype(float) / np.sum(hist2)
    
    kl_divergence = np.sum(np.where(p != 0, p * np.log(p / q), 0))

    return kl_divergence
    
print(
    f"Relative entropy for gray and gray resized_img2: {img_relative_entropy(gray, resized_img2.resize((resized_img2.size[0] * 2, resized_img2.size[1] * 2)))}")
print(
    f"Relative entropy for gray and gray resized_img4: {img_relative_entropy(gray, resized_img4.resize((resized_img4.size[0] * 4, resized_img4.size[1] * 4)))} \n\n")
    
print(
    f"Relative entropy for gray and gray q_img_8: {img_relative_entropy(gray, q_img_8)}")
print(
    f"Relative entropy for gray and gray q_img_16: {img_relative_entropy(gray, q_img_16)}")
print(
    f"Relative entropy for gray and gray q_img_64: {img_relative_entropy(gray, q_img_64)} \n\n")
    
print(
    f"Relative entropy for gray and gray q_resized_img2_8: {img_relative_entropy(gray, q_resized_img2_8.resize((q_resized_img2_8.size[0] * 2, q_resized_img2_8.size[1] * 2)))}")
print(
    f"Relative entropy for gray and gray q_resized_img2_16: {img_relative_entropy(gray, q_resized_img2_16.resize((q_resized_img2_16.size[0] * 2, q_resized_img2_16.size[1] * 2)))}")
print(
    f"Relative entropy for gray and gray q_resized_img2_64: {img_relative_entropy(gray, q_resized_img2_64.resize((q_resized_img2_16.size[0] * 2, q_resized_img2_16.size[1] * 2)))} \n\n")
    
print(
    f"Relative entropy for gray and gray q_resized_img4_8: {img_relative_entropy(gray, q_resized_img4_8.resize((q_resized_img4_8.size[0] * 4, q_resized_img4_8.size[1] * 4)))}")
print(
    f"Relative entropy for gray and gray q_resized_img4_16: {img_relative_entropy(gray, q_resized_img4_16.resize((q_resized_img4_16.size[0] * 4, q_resized_img4_16.size[1] * 4)))}")
print(
    f"Relative entropy for gray and gray q_resized_img4_64: {img_relative_entropy(gray, q_resized_img4_64.resize((q_resized_img4_64.size[0] * 4, q_resized_img4_64.size[1] * 4)))} \n\n")

print(
    f"Relative entropy for gray and gray restored_img2_nearest: {img_relative_entropy(gray, restored_img2_nearest)}")
print(
    f"Relative entropy for gray and gray restored_img2_bilinear: {img_relative_entropy(gray, restored_img2_bilinear)}")
print(
    f"Relative entropy for gray and gray restored_img2_bicubic: {img_relative_entropy(gray, restored_img2_bicubic)} \n\n")
    
print(
    f"Relative entropy for gray and gray restored_img4_nearest: {img_relative_entropy(gray, restored_img4_nearest)}")
print(
    f"Relative entropy for gray and gray restored_img4_bilinear: {img_relative_entropy(gray, restored_img4_bilinear)}")
print(
    f"Relative entropy for gray and gray restored_img4_bicubic: {img_relative_entropy(gray, restored_img4_bicubic)} \n\n")


