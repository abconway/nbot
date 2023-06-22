from PIL import Image
import numpy as np

from config import config


def get_word_arrays():
    im_command_word = Image.open('assets/command_word.png')
    array_command_word = np.delete(np.asarray(im_command_word), 3, axis=2) 
   
    return (
        array_command_word,
    )
