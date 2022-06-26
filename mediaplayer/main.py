from generator import Generator
from selector import Selector
from downloader import Downloader
from processor import Processor
import os

columns, rows = os.get_terminal_size()

def img_local(path_input, width_input=columns):
    image = Selector.imageAscii(path_input, int(width_input))
    return image

def img_online(link_input, save_path, file_name, width_input=columns):
    Downloader.download_image(link_input, save_path, file_name)
    image = Selector.imageAscii(save_path+file_name, int(width_input))
    os.remove(save_path+file_name)
    return image

def video_gif_local(path_input, width_input=columns):
    Selector.video_ascii(path_input, int(width_input))

def video_online(link_input, save_path, file_name, width_input=columns):
    Downloader.download_yt_video(link_input, save_path, file_name)
    Selector.video_ascii(save_path + file_name, int(width_input))
    os.remove(save_path + file_name)

def video_thumb_online(yt_link, save_path, file_name, width_input=columns, delete=0):
    Downloader.download_image(Downloader.get_yt_thumb(yt_link), save_path, file_name)
    image = Selector.imageAscii(save_path + file_name, int(width_input))
    if delete == 0:
        os.remove(save_path + file_name)
    return image

def gif_online(link_input, save_path, file_name, width_input=columns):
    Downloader.download_image(link_input, save_path, file_name)
    Selector.video_ascii(save_path + file_name, 100)
    os.remove(save_path + file_name)

def save_img_text(image, save_path):
    Generator.saveInText(image, save_path)

def save_img_image(image, path_input, width_input, save_path):
    Generator.saveInImage(image, path_input, int(width_input), save_path)

#######################################################################

print("Executando main.py")