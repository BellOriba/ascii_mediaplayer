import requests
from processor import Processor
import re

class Downloader:

    def get_stream_video_itag(video_ob):
        streams = [str(video_ob.streams[i]) for i in range(len(video_ob.streams)-1)]
        regex = '<Stream: itag="\d{2,3}" mime_type="video/webm" res="1080p" fps="\d{1,2}fps" vcodec="[a-zA-Z0-9_.]+" progressive="False" type="video">'
        for stream in streams:
            match = re.search(regex, stream)
            if match != None:
                right_stream = match
                continue
        stream_itag = re.findall('itag="(\d{1,3})"', str(right_stream))
        return stream_itag
    
    def download_yt_video(path, output_path, file_name):
        video_ob = Processor.getVideo(path)
        itag = Downloader.get_stream_video_itag(video_ob)
        yt_stream = video_ob.streams.get_by_itag(itag[0])
        yt_stream.download(output_path, file_name)
    
    def get_yt_thumb(path):
        video_ob = Processor.getVideo(path)
        return video_ob.thumbnail_url

    def download_image(path, save_path, file_name):
        with open(save_path + file_name, 'wb') as handle:
            response = requests.get(path, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

def main() -> None:
    print("Running downloader.py directly")

if __name__ == "__main__":
    main()
