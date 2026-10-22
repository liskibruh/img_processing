import numpy as np
import cv2
from scipy.signal import convolve2d
from utils import load_img, show_img, show_iminfo

def apply_filter(inp, kernel, mode='same', boundary='symm', fill_val=0, inspect_ch=0):
    if not kernel.dtype=='np.float32':
        kernel = kernel.astype(np.float32)
    
    # kernel = kernel / float(kernel.size)
        
    if inp.ndim > 2 and inp.shape[2] ==3:
        inp = inp[:, :, inspect_ch].astype(np.float32)
    
    convolved = convolve2d(inp, kernel, mode=mode, boundary=boundary, fillvalue=fill_val).clip(0, 255)
    
    return convolved

if __name__ == "__main__":
    im_root = "./sample_images/"
    im_name = "images.jpg"
    
    im = load_img(im_root, im_name)
    show_iminfo(im)
    show_img(im[:, :, 0])
    
    # kernel = np.array([
    #     [0, -1, 0],
    #     [-1, 5, -1],        # contrast
    #     [0, -1, 0]
    # ])
    
    # kernel = np.array([
    #     [1, 1, 1],
    #     [1, 1, 1],        # blur
    #     [1, 1, 1]
    # ]) / 9.0
    
    # kernel = np.array([
    #     [-1, 0, 1],
    #     [-2, 0, 2],         # edge
    #     [-1, 0, 1]
    # ])
    
    kernel = np.array([
        [2, -1, 0],
        [-1, 1, 1],         # emboss
        [0, 0, 2]
    ])
    
    inp = im
    # inp = np.zeros((3, 3))
    # mid_h, mid_w = inp[0].size//2, inp[1].size//2
    
    # inp[mid_h, mid_w] = 1.0
        
    g = apply_filter(inp, kernel, boundary='fill')

    print(g[:10, :10])
    show_img(g)