import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def image_info(img):
    print(type(img))
    print(img.shape)
    print(img.ndim)
    print(img.dtype)
    print(img.size)
    print(img.itemsize)
    print(img.nbytes)

def grayscale(img):
    gray = ((0.299 * img[:, :, 0]) +(0.587 * img[:, :, 1]) +(0.114 * img[:, :, 2])).astype(np.uint8)
    return gray

def brightness(img):
    bright = img.astype(np.uint16)
    bright = bright + 50
    bright = np.clip(bright, 0, 255)
    return bright.astype(np.uint8)

def darkness(img):
    dark = img.astype(np.int16)
    dark = dark - 50
    return np.clip(dark, 0, 255).astype(np.uint8)

def invert(img):
    return 255 - img

def contrast(img):
    contrast = 1.2 * img
    return np.clip(contrast, 0, 255).astype(np.uint8)

def red_channel(img):
    red = np.zeros_like(img)
    red[:, :, 0] = img[:, :, 0]
    return red

def green_channel(img):
    green = np.zeros_like(img)
    green[:, :, 1] = img[:, :, 1]
    return green

def blue_channel(img):
    blue = np.zeros_like(img)
    blue[:, :, 2] = img[:, :, 2]
    return blue

def histogram(gray):
    hist = np.zeros(256, dtype=np.int32)

    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):
            val = gray[i, j]
            hist[val] += 1

    return hist

def binary_threshold(gray, threshold=128):
    mask = gray > threshold
    binary = np.zeros_like(gray)
    binary[mask] = 255
    return binary