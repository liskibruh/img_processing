import numpy as np
import cv2
from utils import load_img, show_img, show_iminfo

if __name__ == "__main__":
    
    img = np.zeros((1000, 1000, 3), dtype=np.uint8)
    
    img[:, :, 0] = 20
    img[:, :, 1] = 40
    img[:, :, 2] = 25
    
    
    show_img(img)
    