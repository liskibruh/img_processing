import numpy as np
import matplotlib.pyplot as plt
from utils import load_img, show_img, show_iminfo

def plot_hist(img):
    img = img.copy()
    
    id2color = {0: 'blue', 1: 'green', 2: 'red'}
    
    for i in range(img.shape[2]):
        vals, counts = np.unique(img[:, :, i], return_counts=True)
        plt.plot(vals, counts, color=f'tab:{id2color[i]}', linewidth=1)
    
    plt.title("Color channel PDF")
    plt.xlabel("Intensity Values")
    plt.ylabel("Count")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    im_root = "./sample_images/"
    im_name = "images.jpg"
    
    im = load_img(im_root, im_name)
    show_iminfo(im)
    show_img(im)
    plot_hist(im)
    