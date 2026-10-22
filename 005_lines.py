import numpy as np
import cv2
from utils import show_img, plot_line_on_img

if __name__ == "__main__":
    l1_coeff = np.array([200, 400, 2])
    l2_coeff = np.array([500, 200, 3])
    
    # intersection of two lines is the cross product of both lines
    intersect_pt = np.cross(l1_coeff, l2_coeff)

    # conversion to cartisian coordinates
    w = intersect_pt[2]
    
    x_cart = intersect_pt[0]/w
    y_cart = intersect_pt[1]/w
    
    print(x_cart, y_cart)