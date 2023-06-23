from PIL import Image
import numpy as np

from config import config


def get_number_arrays():
    im = Image.open('assets/font_numbers.png')
    im_0 = im.crop(config['numbers']['0'])
    array_0 = np.delete(np.asarray(im_0), 3, axis=2) 
    im_1 = im.crop(config['numbers']['1'])
    array_1 = np.delete(np.asarray(im_1), 3, axis=2)
    im_2 = im.crop(config['numbers']['2'])
    array_2 = np.delete(np.asarray(im_2), 3, axis=2)
    im_3 = im.crop(config['numbers']['3'])
    array_3 = np.delete(np.asarray(im_3), 3, axis=2)
    im_4 = im.crop(config['numbers']['4'])
    array_4 = np.delete(np.asarray(im_4), 3, axis=2)
    im_5 = im.crop(config['numbers']['5'])
    array_5 = np.delete(np.asarray(im_5), 3, axis=2)
    im_6 = im.crop(config['numbers']['6'])
    array_6 = np.delete(np.asarray(im_6), 3, axis=2)
    im_7 = im.crop(config['numbers']['7'])
    array_7 = np.delete(np.asarray(im_7), 3, axis=2)
    im_8 = im.crop(config['numbers']['8'])
    array_8 = np.delete(np.asarray(im_8), 3, axis=2)
    im_9 = im.crop(config['numbers']['9'])
    array_9 = np.delete(np.asarray(im_9), 3, axis=2)
    return (
        array_0,
        array_1,
        array_2,
        array_3,
        array_4,
        array_5,
        array_6,
        array_7,
        array_8,
        array_9,
    )


NUM_0, NUM_1, NUM_2, NUM_3, NUM_4, NUM_5, NUM_6, NUM_7, NUM_8, NUM_9 = get_number_arrays()


def get_number(im: Image):
    num_array = np.asarray(im)
    if np.array_equal(num_array, NUM_0):
        return 0
    elif np.array_equal(num_array, NUM_1):
        return 1
    elif np.array_equal(num_array, NUM_2):
        return 2
    elif np.array_equal(num_array, NUM_3):
        return 3
    elif np.array_equal(num_array, NUM_4):
        return 4
    elif np.array_equal(num_array, NUM_5):
        return 5
    elif np.array_equal(num_array, NUM_6):
        return 6
    elif np.array_equal(num_array, NUM_7):
        return 7
    elif np.array_equal(num_array, NUM_8):
        return 8
    elif np.array_equal(num_array, NUM_9):
        return 9
    else:
        return 0