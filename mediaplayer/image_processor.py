from PIL import Image

class Processor:

    def getImage(image_path):
        return Image.open(image_path)

    def getPixelsColors(image, rows=None, collums=None, with_coordinates=0):
        """
        return a list of tuples with the coordinate and other tuple with the RGBA values of each pixel [(int x, int y, (int r, int g, int b, int a))]

        if the second and third values are not entered, the will be assigned to the full value of width and height of the image

        the forth value indicates if the returning tuple will have the coordinates values of the pixel
        """
        if rows is None or rows == "":
            rows = image.width
        else:
            rows = int(rows)

        if collums is None or collums == "":
            collums = image.height
        else:
            collums = int(collums)

        all_colors = []

        if with_coordinates == 0:
            all_colors = [image.getpixel((i, j)) for j in range(0, collums) for i in range(0, rows)]
        else:
            all_colors = [(i, j, image.getpixel((i, j))) for j in range(0, collums) for i in range(0, rows)]

        return all_colors
    
    ## All PIL.Image attributes
    """
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

    for i in range(0, rows):
                for j in range(0, collums):
                    all_colors.append(image.getpixel((i, j)))
    """

def main() -> None:
    print("Executando image_processor.py diretamente")

if __name__ == "__main__":
    main()
