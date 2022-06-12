from generator import Generator
from selector import Selector

def main():
    print("If the image is rendered with blank lines between the characters, remove the '\\n' from the function image_ascii in the type_selector.py")
    print("Enter the type of converter you will use:")
    user_input = input("""
    Image Converter (B&W) : 0
    Image Converter (Color) : 1
    Video Converter (B&W) : 2
    Video Converter (Color) : 3

    Type the value here: """)
    if user_input == "0":
        image = Selector.image_ascii("./path/example.png")
        print(image)
        Generator.saveInText(image, "./path/example.txt")
    else:
        print("Not yet implemented.")

print("Executando main.py")
main()
