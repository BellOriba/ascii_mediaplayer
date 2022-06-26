from generator import Generator
from processor import Processor
import sys
import os
import cv2
from PIL import Image

class Selector:

    columns, rows = os.get_terminal_size()

    def imageAscii(path, new_width=columns-1):
        image = Processor.getImage(path)
        ascii_image = Generator.generateAscii(image, new_width)

        sys.stdout.write(ascii_image)
        return ascii_image

    def video_ascii(path, new_width=columns-1):
        cap = cv2.VideoCapture(path)
        while True:
            ret, frame = cap.read()
            while ret:
                cv2.imshow("frame", frame)
                image_frame = Image.fromarray(frame)
                Generator.generateNewFrame(image_frame, new_width)
                cv2.waitKey(1)
                ret, frame = cap.read()
            break

def main() -> None:
    print("Running selector.py directly")

if __name__ == "__main__":
    main()
