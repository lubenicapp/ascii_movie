from PIL import Image
import numpy as np
from math import floor

GREY_SCALE = ' `^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def asciify_image(image: np.array, lines, columns) -> str:
    tile_w = image.shape[1]//columns
    tile_h = image.shape[0]//lines
    min_val = np.min(image)
    max_val = np.max(image)
    r = ''
    for i in range(lines):
        for j in range(columns):
            value = (np.average(image[tile_h*i:tile_h*(i+1), tile_w*j:tile_w*(j+1)]))
            char = grey_value_to_char(value, min_val, max_val)
            r += char
        r += '\n'
    return r


def grey_value_to_char(val, min_val, max_val):
    step = (max_val - min_val)/len(GREY_SCALE)
    return GREY_SCALE[floor((val - min_val) * step / len(GREY_SCALE))]


vec_grey_value_to_char = np.vectorize(grey_value_to_char)
