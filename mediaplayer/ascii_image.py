from PIL import Image

CHAR_LIST_BLOCKS = ['░', '▒', '▓', '█'] # Not already implemented
CHAR_LIST_CHARS = ['@', '#', '&', "$", "%", "?", "*", "+", ";", ":", ",", "."]

class ImageGenerator:

    def convertToAscii(image):
        """
        convert each pixel in a image to a ASCII character.
        """
        all_pixels = image.getdata()
        characters = "".join([CHAR_LIST_CHARS[pixel//25] for pixel in all_pixels])
        return characters

    def convertToAsciiColor():
        pass

def main() -> None:
    print("Running ascii_image.py directly")

if __name__ == "__main__":
    main()
