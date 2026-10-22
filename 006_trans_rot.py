import numpy as np
from utils import show_img, plot_line_on_img, load_img, show_iminfo

def apply_transformation(img, H):
    
    h, w = img.shape
    grid = np.indices((h,w)).reshape(2, h*w)[::-1]
    ones = np.ones((1, len(grid[0])), dtype=np.int8)
    homo_inds = np.concat((grid, ones), axis=0)
    
    trans_inds = H @ homo_inds
    
    trans_inds = trans_inds[:2]
    inds = homo_inds[:2]
    
    trans_xs = np.rint(trans_inds[0]).astype(int)
    trans_ys = np.rint(trans_inds[1]).astype(int)

    valid = (
        (trans_xs>0) & (trans_xs<w) &
        (trans_ys>0) & (trans_ys<h)
    )
    
    trans_img = np.zeros((h, w), dtype=np.uint8)
    intensities = img.ravel()
    trans_img[trans_ys[valid], trans_xs[valid]] = intensities[valid]

    return trans_img    


if __name__ == "__main__":
    im_root = "./sample_images/"
    im_name = "images.jpg"
    
    im = load_img(im_root, im_name)
    im = im[:, :, 1] # extract a single channel image
    # h, w = 3, 3
    
    H = np.array(
        [[1, 0,  15],
         [0, 1,  25],
         [0, 0,  1 ]])
    
    rot_img = apply_transformation(im, H)
    
    show_img(im)
    show_img(rot_img)
    
    