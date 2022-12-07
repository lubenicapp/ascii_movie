from PIL import Image
import numpy as np
from math import floor

# GREY_SCALE = '`.-:_,^=;><+!rc*/z?sLTv)J7#$Bg0MNWQ%&@'
# GREY_SCALE = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'
GREY_SCALE = ' .:-_=+*#%@'

STEP = 255 / len(GREY_SCALE)

OFFSET = 15


def asciify_image(image: np.array, lines, columns) -> str:
    tile_w, tile_h = image.shape[1]//columns, image.shape[0]//lines

    r = ''
    for i in range(lines):
        # absolutely don't understand why is it better centered with this offset
        for j in range(OFFSET, columns + OFFSET):
            value = round((np.average(image[tile_h*i:tile_h*(i+1), tile_w*j:tile_w*(j+1)])))
            char = grey_value_to_char(value)
            r += char
        r += '\n'
    return r


def grey_value_to_char(val, step=STEP):
    return GREY_SCALE[min(floor((val / step)), len(GREY_SCALE) - 1)]


vec_grey_value_to_char = np.vectorize(grey_value_to_char)
