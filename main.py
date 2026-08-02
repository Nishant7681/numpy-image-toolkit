import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from image_loader import img
from filters import blur, sharpen, edge_detection
from transform import Horizontal_flip, Vertical_flip, Crop, Resize, Rotate
from utils import (
    image_info,
    grayscale,
    brightness,
    darkness,
    invert,
    contrast,
    red_channel,
    green_channel,
    blue_channel,
    histogram,
    binary_threshold,
)

image_info(img)

gray = grayscale(img)

bright = brightness(img)

dark = darkness(img)

invert_img = invert(img)

contrast_img = contrast(img)

flip_h = Horizontal_flip(img)

flip_v = Vertical_flip(img)

crop_img = Crop(img)

pil_img = Image.fromarray(img)

resize_img = Resize(pil_img)
resize_img.save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/resize.jpg")

rotate_img = Rotate(pil_img)
rotate_img.save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/rotate.jpg")

blur_img = blur(pil_img)
blur_img.save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/blur.jpg")

sharp_img = sharpen(pil_img)
sharp_img.save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/sharp.jpg")

edge_img = edge_detection(pil_img)
edge_img.save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/edge.jpg")


red = red_channel(img)
Image.fromarray(red).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/red.jpg")

green = green_channel(img)
Image.fromarray(green).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/green.jpg")

blue = blue_channel(img)
Image.fromarray(blue).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/blue.jpg")

hist = histogram(gray)

plt.bar(np.arange(256), hist)

plt.xlabel("Intensity")

plt.ylabel("Frequency")

plt.title("Grayscale Histogram")

plt.tight_layout()

plt.savefig("C:/Users/HP/c tutorial/numpy-image-toolkit/output/histogram.png")

plt.show()

# Binary Thresholding (Black & White)

binary = binary_threshold(gray)

Image.fromarray(gray).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/gray.jpg")
Image.fromarray(bright).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/bright.jpg")
Image.fromarray(dark).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/dark.jpg")
Image.fromarray(invert_img).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/invert.jpg")
Image.fromarray(contrast_img).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/contrast.jpg")
Image.fromarray(flip_h).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/flip_h.jpg")
Image.fromarray(flip_v).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/flip_v.jpg")
Image.fromarray(crop_img).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/crop.jpg")
Image.fromarray(binary).save("C:/Users/HP/c tutorial/numpy-image-toolkit/output/binary.jpg")