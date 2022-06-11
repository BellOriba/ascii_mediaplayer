from type_selector import Selector

print("Executando main.py")

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
        Selector.image_ascii("./path/example.jpg", 175)
    else:
        print("Not yet implemented.")

main()