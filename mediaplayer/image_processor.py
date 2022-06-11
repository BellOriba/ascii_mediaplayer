from PIL import Image

class Processor:

    def getImage(image_path):
        """
        create a PIL.Image Object
        """
        return Image.open(image_path)

    def resizeImage(image, new_width=200):
        width, height = image.size
        ratio = height / width / 1.65
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width, new_height))
        return resized_image

    def convertPixelToGray(image):
        """
        convert each pixel to grayscale
        """
        gray_img = image.convert("L")
        return gray_img

    # Not already implemented
    def getPixelsColors(image, rows=None, columns=None, with_coordinates=0):
        """
        return a list of tuples with the coordinate and other tuple with the RGBA values of each pixel [(int x, int y, (int r, int g, int b, int a))]

        if the second and third values are not entered, the will be assigned to the full value of width and height of the image

        the forth value indicates if the returning tuple will have the coordinates values of the pixel
        """
        if rows is None or rows == "":
            rows = image.width
        else:
            rows = int(rows)

        if columns is None or columns == "":
            columns = image.height
        else:
            columns = int(columns)

        all_colors = []

        if with_coordinates == 0:
            all_colors = [image.getpixel((i, j)) for j in range(0, columns) for i in range(0, rows)]
        else:
            all_colors = [(i, j, image.getpixel((i, j))) for j in range(0, columns) for i in range(0, rows)]

        return all_colors

def main() -> None:
    print("Executando image_processor.py diretamente")

if __name__ == "__main__":
    main()
