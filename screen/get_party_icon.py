from PIL import Image

from config import config


def get_party_icon(image, ref_loc, icon_size='32x32') -> Image:
    party_icon_width = config['icon_sizes'][icon_size]['party_icon']['width']
    party_icon_height = config['icon_sizes'][icon_size]['party_icon']['height']
    party_icon_global_offset = config['icon_sizes'][icon_size]['party_icon']['global_offset']   
    
    box = (
        ref_loc[0] + party_icon_global_offset[0],
        ref_loc[1] + party_icon_global_offset[1], 
        ref_loc[0] + party_icon_global_offset[0] + party_icon_width, 
        ref_loc[1] + party_icon_global_offset[1] + party_icon_height,
    )

    im1 = image.crop(box)
    return im1
