from PIL import Image

from config import config


def get_battle_icon(image, resolution='1920x1080') -> Image:   
    box = config['resolutions'][resolution]['in_battle']['sword_icon']
    im1 = image.crop(box)
    return im1
