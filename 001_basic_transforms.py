import numpy as np
from utils import load_img, show_img

def linear_blend(im1, im2, alpha=0.5):
    blend = ((1 - alpha) * im1) + (alpha * im2)
    return blend.astype(np.uint8)

def gamma_correct(img, gamma=2.2):
    img = img ** 1/gamma
    return img.astype(np.uint8)
    
if __name__ == "__main__":
    im_root = "./sample_images/"
    im1_name = "0000136.jpg"
    im2_name = "0000178.jpg"
    
    im1 = load_img(im_root, im1_name)
    im2 = load_img(im_root, im2_name)
    
    # dyadic operator, linear blend
    blended_im = linear_blend(im1, im2, alpha=0.5)
    
    # gamma correction
    gamma_corr_im = gamma_correct(im1, gamma=2.2)

    show_img(blended_im)