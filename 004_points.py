import numpy as np
from utils import plot_line_on_img, show_img

def lineq2linepts(line_coeff):
    a, b, c = line_coeff
    x_range = np.linspace(0, 200, 400, endpoint=True)
    
    if b!=0:
        y_range = (-a*x_range - c) / b
    else:
        x_range = np.full_like(x_range, -c/a)
        y_range = np.linspace(0, 200, len(x_range))
    
    line = np.stack((x_range, y_range), axis=0)
    
    return line
        

if __name__ == "__main__":
    pt1 = np.array([2, 5, 1], dtype=np.int16)
    pt2 = np.array([4, 8, 1], dtype=np.int16)
    
    line_coeff = np.cross(pt1, pt2)
    line = lineq2linepts(line_coeff)
    
    img = np.zeros((200, 200), dtype=np.uint8)
    
    img = plot_line_on_img(line, img)
    show_img(img)
    
    