from PIL import Image
import numpy as np

from config import config


def get_icon_arrays():
    im_sword_icon = Image.open('assets/sword_icon.png')
    array_sword_icon = np.delete(np.asarray(im_sword_icon), 3, axis=2) 
    im_sword_active_icon = Image.open('assets/sword_active_icon.png')
    array_sword_active_icon = np.delete(np.asarray(im_sword_active_icon), 3, axis=2)
    im_party_icon = Image.open('assets/party_icon.png')
    array_party_icon = np.delete(np.asarray(im_party_icon), 3, axis=2)

    return (
        array_sword_icon,
        array_sword_active_icon,
        array_party_icon,
    )
