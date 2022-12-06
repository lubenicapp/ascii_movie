from PIL import Image
import numpy as np
from math import floor

GREY_SCALE = ' `^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
STEP = 255 / len(GREY_SCALE)


def asciify_image(image: np.array, lines, columns) -> str:
    tile_w, tile_h = image.shape[1]//columns, image.shape[0]//lines

    r = ''
    for i in range(lines):
        for j in range(columns):
            value = (np.average(image[tile_h*i:tile_h*(i+1), tile_w*j:tile_w*(j+1)]))
            char = grey_value_to_char(value)
            r += char
        r += '\n'
    return r


def grey_value_to_char(val):
    return GREY_SCALE[min(floor((val * STEP) / len(GREY_SCALE)), len(GREY_SCALE) - 1)]


vec_grey_value_to_char = np.vectorize(grey_value_to_char)
