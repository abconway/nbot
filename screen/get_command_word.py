from PIL import Image

from config import config


def get_command_word(image: Image, ref_loc, icon_size='32x32') -> Image:    
    command_word_width = config['icon_sizes'][icon_size]['command_word']['width']
    command_word_height = config['icon_sizes'][icon_size]['command_word']['height']
    command_word_global_offset = config['icon_sizes'][icon_size]['command_word']['global_offset']   
    
    box = (
        ref_loc[0] + command_word_global_offset[0],
        ref_loc[1] + command_word_global_offset[1], 
        ref_loc[0] + command_word_global_offset[0] + command_word_width, 
        ref_loc[1] + command_word_global_offset[1] + command_word_height,
    )

    im1 = image.crop(box)
    return im1
