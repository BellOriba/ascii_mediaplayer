from type_selector import Selector

print("Executando main.py")

def main():
    print("Enter the type of converter you will use:")
    user_input = input("""
    Image Converter (B&W) : 0
    Image Converter (Color) : 1
    Video Converter (B&W) : 2
    Video Converter (Color) : 3

    Type the value here: """)
    if user_input == "0":
        Selector.image_ascii("./img_test/juliusCaesar.png")
    else:
        print("Not yet implemented.")

main()