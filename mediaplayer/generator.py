from processor import Processor

CHAR_LIST_BLOCKS = ['░', '▒', '▓', '█'] # Not already implemented
CHAR_LIST = ['@', '#', '&', "$", "%", "?", "*", "+", ";", ":", ",", "."]

class Generator:

    def __convertToAscii(pix_colors) -> str:
        """
        convert each pixel in a image to a ASCII character.
        """
        characters = "".join([CHAR_LIST[pixel//25] for pixel in pix_colors])
        return characters

    def generateAscii(image, new_width):
        new_image = Generator.__convertToAscii(Processor.getPixelsColors(Processor.convertImageToGray(Processor.resizeImage(image, new_width))))
        pixel_count = len(new_image)
        ascii_image = "\n".join([new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width)])
        return ascii_image

    def convertToAsciiColor():
        pass

    def saveInText(image, path):
        """
        return None.
        
        Save the ASCII art in a txt file.
        """
        with open(path, "w") as f:
            f.write(image)

    def saveInImage(image):
        """
        return None.
        
        Save the ASCII art in a png file.
        """
        pass

def main() -> None:
    print("Running generator.py directly")

if __name__ == "__main__":
    main()
