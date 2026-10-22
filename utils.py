import numpy as np
import cv2
import os

def load_img(root, imname):
    im_pth = os.path.join(root, imname)
    return cv2.imread(im_pth)

def show_img(im):
    im = im.astype(np.uint8)
    cv2.imshow('im-window', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_iminfo(im):
    print(f"im dtype: {im.dtype}")
    print(f"image shape: {im.shape}")
    print(f"max in each channel: {np.max(im, axis=(0,1))}")
    print(f"min in each channel: {np.min(im, axis=(0,1))}")
    print(f"mean of each channel: {np.mean(im, axis=(0,1))}")
    print(f"="*64)
    
def plot_line_on_img(line1, img):
        
    lstart = tuple(line1.T[0].astype(int).tolist())
    lend = tuple(line1.T[-1].astype(int).tolist())
    
    cv2.line(img, lstart, lend, color=255, thickness=2)
    
    return img