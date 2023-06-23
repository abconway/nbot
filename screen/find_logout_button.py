from typing import Tuple

import cv2
import numpy as np
from PIL import Image


def find_logout_button(image: Image) -> Tuple[int, int]:
    logout_button_image = cv2.imread('assets/logout_button.png')
    result = cv2.matchTemplate(np.asarray(image), logout_button_image, cv2.TM_CCOEFF)
    _, _, _, max_loc = cv2.minMaxLoc(result)
    return max_loc
