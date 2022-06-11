from PIL import Image, ImageColor


CHAR_LIST = ['░', '▒', '▓', '█']

im = Image.open("img_test/Adamastor.png")
print(im)

## All PIL.Image attributes
print("""
filename = {}
format = {}
mode = {}
size = {}
width = {}
height = {}
palette = {}
info = {}
is_animated = {}
n_frames = {}
""".format(im.filename, im.format, im.mode, im.size, im.width, im.height, im.palette, im.info, im.is_animated, im.n_frames))

