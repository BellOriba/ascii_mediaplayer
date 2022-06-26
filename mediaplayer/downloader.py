import requests
from processor import Processor

class Downloader:
    
    def download_yt_video(path, output_path, file_name):
        video_ob = Processor.getVideo(path)
        yt_stream = video_ob.streams.get_by_itag(248)
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
    Downloader.download_image("https://criticalhits.com.br/wp-content/uploads/2021/07/konosuba-megumin-random-pn-n.jpg", "./img_test/", "test.png")
    print("Running downloader.py directly")

if __name__ == "__main__":
    main()
