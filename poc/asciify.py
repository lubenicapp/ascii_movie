import numpy as np
from math import floor

# GREY_SCALE = '`.-:_,^=;><+!rc*/z?sLTv)J7#$Bg0MNWQ%&@'
# GREY_SCALE = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'
GREY_SCALE = ' .:-_=+*#%@'

STEP = 255 / len(GREY_SCALE)


def asciify_image(image: np.array, lines, columns) -> str:
    tile_w, tile_h = image.shape[1]//columns, image.shape[0]//lines

    pixel_loss_w = image.shape[1] - tile_w * columns
    pixel_loss_h = image.shape[0] - tile_h * lines

    column_loss = round(pixel_loss_w / tile_w)
    line_loss = round(pixel_loss_h / tile_h)

    r = ''
    for i in range(line_loss//2, lines + line_loss//2):
        for j in range(column_loss//2, columns + column_loss//2):
            value = round((np.average(image[tile_h*i:tile_h*(i+1), tile_w*j:tile_w*(j+1)])))
            char = grey_value_to_char(value)
            r += char
        r += '\n'
    return r


def grey_value_to_char(val, step=STEP):
    return GREY_SCALE[min(floor((val / step)), len(GREY_SCALE) - 1)]

