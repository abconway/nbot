from typing import Tuple

import cv2
import numpy as np
from PIL import Image

BOOMER = {
    'name': 'Boomer',
    'image': cv2.imread('assets/monsters/battle_future-verity_boomer.png'),
    'threshold': 0.6,
    'hp': 98,
}
DARK_HYDRA = {
    'name': 'Dark Hydra',
    'image': cv2.imread('assets/monsters/battle_future-verity_dark-hydra.png'),
    'threshold': 0.6,
    'hp': 350,
}
DEMI_SLAVE = {
    'name': 'Demi Slave',
    'image': cv2.imread('assets/monsters/battle_future-verity_demi-slave.png'),
    'threshold': 0.6,
    'hp': 87,
}
POLTERGEIST = {
    'name': 'Poltergeist',
    'image': cv2.imread('assets/monsters/battle_future-verity_poltergeist.png'),
    'threshold': 0.6,
    'hp': 87,
}
PUNY_PUMPKIN = {
    'name': 'Puny Pumpkin',
    'image': cv2.imread('assets/monsters/battle_anywhere_puny-pumpkin.png'),
    'threshold': 0.6,
    'hp': 5,
}
WATCHER = {
    'name': 'Watcher',
    'image': cv2.imread('assets/monsters/battle_future-verity_watcher.png'),
    'threshold': 0.6,
    'hp': 85,
}
MONSTERS = [BOOMER, DARK_HYDRA, DEMI_SLAVE, PUNY_PUMPKIN, POLTERGEIST, WATCHER]


def identify_monsters(image: Image, monsters=MONSTERS) -> Tuple[int, int]:
    found_monsters = []
    for monster in MONSTERS:
        result = cv2.matchTemplate(np.asarray(image), monster['image'], cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val >= monster['threshold']:
            (yCoords, xCoords) = np.where(result >= max_val*0.99)
            coords = list(zip(xCoords, yCoords))
            for index, coord in enumerate(coords):
                if len(coords) == 1:
                    name = monster['name']
                else:
                    name = f'{monster["name"]}-{index + 1}'
                found_monsters.append((coord[0], name))
    found_monsters.sort()
    if len(found_monsters) == 1:
        return (found_monsters[0][1],)
    else:
        _, names = zip(*found_monsters)
        return names


if __name__ == '__main__':
    image = Image.open('test.png')
    print(identify_monsters(image))