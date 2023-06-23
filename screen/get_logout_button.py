from PIL import Image

from config import config


def get_logout_button(image, ref_loc, icon_size='32x32') -> Image:
    logout_button_width = config['icon_sizes'][icon_size]['logout_button']['width']
    logout_button_height = config['icon_sizes'][icon_size]['logout_button']['height'] 
    
    box = (
        ref_loc[0],
        ref_loc[1], 
        ref_loc[0] + logout_button_width, 
        ref_loc[1] + logout_button_height,
    )

    im1 = image.crop(box)
    return im1
