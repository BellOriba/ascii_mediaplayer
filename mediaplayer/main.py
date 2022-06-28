from selector import Selector

print("Running main.py\n\n")

image_ascii = Selector.img_online("https://i.pinimg.com/originals/12/e5/b0/12e5b0ed7784a3177fa8032cf88c3942.jpg", "./", "megumin.png", 900)
Selector.save_img_text(image_ascii, "./test.txt")
