from PIL import Image, ImageDraw, ImageFont

class Processor:

    def getImage(image_path):
        """
        create a PIL.Image Object
        """
        return Image.open(image_path)

    def resizeImage(image, new_width):
        width, height = image.size
        ratio = height / width / 1.65
        new_height = int(new_width * ratio)
        resized_image = image.resize((new_width, new_height))
        return resized_image

    def convertImageToGray(image):
        """
        convert each pixel to grayscale
        """
        gray_img = image.convert("L")
        return gray_img

    def getPixelsColors(image):
        """
        returns a list of tuples with each pixel RGB (for jpg) or RGBA (for png) values
        """
        pix_colors = image.getdata()
        return pix_colors

def main() -> None:
    print("Running processor.py directly")

if __name__ == "__main__":
    main()
