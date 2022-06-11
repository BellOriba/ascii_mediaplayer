from PIL import Image
from ascii_image import ImageGenerator
from image_processor import Processor

class Selector:

    def image_ascii(path, new_width=200):
        image = Processor.getImage(path)
        new_image = ImageGenerator.convertToAscii(Processor.convertPixelToGray(Processor.resizeImage(image, new_width)))

        pixel_count = len(new_image)
        ascii_image = "\n".join([new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width)])

        print(ascii_image)

        with open("examples/ascii_image2.txt", "w") as f:
            f.write(ascii_image)
    
    def image_ascii_color():
        pass

    def video_ascii():
        pass
    
    def video_ascii_color():
        pass

def main() -> None:
    print("Executando type_selector.py diretamente")

if __name__ == "__main__":
    main()
