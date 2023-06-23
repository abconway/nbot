from PIL import Image

from config import config


def get_battle_icon(image, ref_loc, icon_size='32x32') -> Image:
    battle_icon_width = config['icon_sizes'][icon_size]['battle_icon']['width']
    battle_icon_height = config['icon_sizes'][icon_size]['battle_icon']['height']
    battle_icon_global_offset = config['icon_sizes'][icon_size]['battle_icon']['global_offset']   
    
    box = (
        ref_loc[0] + battle_icon_global_offset[0],
        ref_loc[1] + battle_icon_global_offset[1], 
        ref_loc[0] + battle_icon_global_offset[0] + battle_icon_width, 
        ref_loc[1] + battle_icon_global_offset[1] + battle_icon_height,
    )

    im1 = image.crop(box)
    return im1
