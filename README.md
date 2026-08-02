# NumPy Image Toolkit
A beginner-friendly image processing toolkit built with Python, NumPy, Pillow and Matplotlib. It demonstrates fundamental image processing techniques using modular and clean code.

This project performs basic image processing operations such as grayscale conversion, brightness adjustment, contrast enhancement, filtering, histogram generation and binary thresholding.

## Features
- Image Information
- Grayscale Conversion
- Brightness Adjustment
- Darkness Adjustment
- Image Inversion
- Contrast Enhancement
- Horizontal Flip
- Vertical Flip
- Image Cropping
- Image Resize
- Image Rotation
- Gaussian Blur
- Sharpen Filter
- Edge Detection
- RGB Channel Separation
- RGB Channel Extraction
- Grayscale Histogram
- Binary Thresholding

## Libraries Used
- NumPy
- Pillow (PIL)
- Matplotlib

## Folder Structure
numpy-image-toolkit/

- images/
- output/
- filters.py
- image_loader.py
- main.py
- transform.py
- utils.py
- README.md
- requirements.txt
- .gitignore

## How to Run
- Install the required libraries.
- Run `main.py`.
- Processed images will be saved in the `output` folder.

## Future Improvements
- Histogram Equalization
- Image Blending
- Image Compression
- Image Scaling
- Noise Reduction
- Adaptive Thresholding

# Output Examples

## Grayscale Conversion

| Before | After |
|--------|-------|
| <img src="images/cat.jpg" width="300"> | <img src="output/gray.jpg" width="300"> |

---

## Brightness Adjustment

| Before | After |
|--------|-------|
| <img src="images/cat.jpg" width="300"> | <img src="output/bright.jpg" width="300"> |

---

## Contrast Enhancement

| Before | After |
|--------|-------|
| <img src="images/cat.jpg" width="300"> | <img src="output/contrast.jpg" width="300"> |

---

## Blur Filter

| Before | After |
|--------|-------|
| <img src="images/cat.jpg" width="300"> | <img src="output/blur.jpg" width="300"> |

---


## Edge Detection

| Before | After |
|--------|-------|
| <img src="images/cat.jpg" width="300"> | <img src="output/edge.jpg" width="300"> |

---

## RGB Channel Extraction

| Red | Green | Blue |
|-----|-------|------|
| <img src="output/red.jpg" width="220"> | <img src="output/green.jpg" width="220"> | <img src="output/blue.jpg" width="220"> |

---

## Grayscale Histogram

<img src="output/histogram.png" width="700">

---

## Binary Thresholding

| Before | After |
|--------|-------|
| <img src="output/gray.jpg" width="300"> | <img src="output/binary.jpg" width="300"> |
