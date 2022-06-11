from PIL import Image
import ascii_image
from image_processor import Processor

image = Processor.getImage("./img_test/Adamastor.png")
Processor.getPixelsColors(image, input("Enter the number of rows: "), input("Enter the number of collums: "))
print("Executando main.py")
