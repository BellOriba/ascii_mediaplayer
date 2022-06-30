from selector import Selector
import argparse
import os
import random

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
random_n = random.randint(100, 999)
file_name = "ascii"+str(random_n)

parser = argparse.ArgumentParser(description="Transform images and videos in ASCII art.")
parser.add_argument('-p', '--path', metavar="", type=str, required=True, help="File path.")
parser.add_argument('-sv', '--save_path', metavar='', type=str, default=desktop, help="Path to save the file.")
parser.add_argument('-fn', '--file_name', metavar='', type=str, default=file_name, help="File name.")
parser.add_argument('-w', '--width', metavar='', type=str, default=None, help="Output width.")

type_path = parser.add_mutually_exclusive_group(required=True)
type_path.add_argument('-l', '--local', action='store_true', help="Used to convert a local file.")
type_path.add_argument('-o', '--online', action='store_true', help="Used to convert a online file.")

type_convert = parser.add_mutually_exclusive_group(required=True)
type_convert.add_argument('-i', '--image', action='store_true', help="Convert a image file to ASCII art.")
type_convert.add_argument('-v', '--video', action='store_true', help="Convert a video file to ASCII art.")
type_convert.add_argument('-g', '--gif', action='store_true', help="Convert a GIF file in ASCII art.")

save_type = parser.add_argument_group('Save options')
save_type.add_argument('-txt', '--txt_save', action='store_true', help="Save the converted image to a TXT file.")
save_type.add_argument('-png', '--png_save', action='store_true', help="Save the converted image to a PNG file.")
args = parser.parse_args()

def main() -> None:

    columns, lines = os.get_terminal_size()


    if args.width == None:
        args.width = columns

    if args.local:
        if args.image:
            image_ascii = Selector.img_local(args.path, args.width)
        elif args.video:
            Selector.video_gif_local(args.path, args.width)
        elif args.gif:
            Selector.video_gif_local(args.path, args.width)
    elif args.online:
        if args.image:
            image_ascii = Selector.img_online(args.path, args.save_path, args.file_name, args.width)
        elif args.video:
            Selector.video_online(args.path, args.save_path, args.file_name+'.webm', args.width)
        elif args.gif:
            Selector.gif_online(args.path, args.save_path, args.file_name+'.gif', args.width)
    
    if args.txt_save:
        Selector.save_img_text(image_ascii, args.save_path+'\\'+args.file_name+'.txt')

    if args.png_save:
        Selector.save_img_image(image_ascii, args.path, args.width, args.save_path+'\\'+args.file_name+'.png')

if __name__ == "__main__":
    main()