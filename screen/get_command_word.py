from PIL import Image

from config import config


def get_command_word(image: Image, resolution='1920x1080') -> Image:    
    box = config['resolutions'][resolution]['in_battle']['command_word']
    im1 = image.crop(box)
    return im1
