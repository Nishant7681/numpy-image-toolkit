from PIL import ImageFilter

def blur(pil_img):
    return pil_img.filter(ImageFilter.BLUR)

def sharpen(pil_img):
    return pil_img.filter(ImageFilter.SHARPEN)

def edge_detection(pil_img):
    return pil_img.filter(ImageFilter.FIND_EDGES)