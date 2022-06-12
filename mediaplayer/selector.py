from generator import Generator
from processor import Processor
import os

class Selector:

    columns, lines = os.get_terminal_size()

    def image_ascii(path, new_width=columns):
        image = Processor.getImage(path)
        ascii_image = Generator.generateAscii(image, new_width)
        return ascii_image

    def image_ascii_color():
        pass

    def video_ascii():
        pass
    
    def video_ascii_color():
        pass

def main() -> None:
    print("Running selector.py directly")

if __name__ == "__main__":
    main()
