
def Horizontal_flip(img):
    return img[:, ::-1, :]

def Vertical_flip(img):
    return img[::-1, :, :]

def Crop(img):
    return img[200:1001, 300:1201, :]

def Resize(pil_img):
    return pil_img.resize((200, 100))

def Rotate(pil_img):
    return pil_img.rotate(-180, expand=True)