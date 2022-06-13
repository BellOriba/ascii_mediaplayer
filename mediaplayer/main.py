from generator import Generator
from selector import Selector
import os
def main():
    print("If the image is rendered with blank lines between the characters, remove the '\\n' from the function image_ascii in the type_selector.py")
    print("Enter the type of converter you will use:")
    print("""
    Image Converter (B&W) : 0
    Image Converter (Color) : 1
    Video/GIF Converter (B&W) : 2
    Video/GIF Converter (Color) : 3""")
    type_input = input("\nType the value here: ")
    width_input = input("\nType the width of the image/video: ")
    path_input = input("\nInsert the path to the file: ")
    if width_input == "":
        columns, rows = os.get_terminal_size()
        width_input = columns-1

    if type_input == "0":
        image = Selector.imageAscii(path_input, int(width_input))
    elif type_input == "2":
        image = Selector.video_ascii(path_input, int(width_input))
    else:
        print("Not yet implemented.")
    if type_input == "0" or type_input == "1":
        save_input = input("\nWant to save your image to a txt file? [Y]/[n] ")
        if save_input == "Y":
            Generator.saveInText(image, "./examples/example.txt")

print("Executando main.py")
main()
