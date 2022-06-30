# ASCII Mediaplayer
![Python Versions](https://img.shields.io/pypi/pyversions/django?logo=python&logoColor=white&style=for-the-badge)

Convert images and videos to ASCII art.

## How to run
### Local Files
**Convert a local image**  
`py main.py -p [file path] -l -i`  
Optional: `-w [output width]`

**Convert a local video**  
`py main.py -p [file path] -l -v`  
Optional: `-w [output width]`

**Convert a local gif**  
`py main.py -p [file path] -l -g`  
Optional: `-w [output width]`

### Online Files
**Convert a online image**  
`py main.py -p [url] -o -i`  
Optional: `-w [output width]`

**Convert a online video**  
`py main.py -p [url] -o -v`  
Optional: `-w [output width]`

**Convert a online gif**  
`py main.py -p [url] -o -g`  
Optional: `-w [output width]`

### Save ASCII
**Save a ASCII image as txt**  
Works for local and online images  
`py main.py -p [file path] -l -i -txt`  
Optional commands:  
- `-w [output width]` -> Width of the output image (default: console width)  
- `-sv [save_path]` -> To choose a folder to save the file (default: desktop)  
- `-fn [filename]` -> To choose a file name (default: ascii+[random number])

**Save a ASCII image as png**
Works only for local images  
`py main.py -p [file path] -l -i -png`  
Optional commands:  
- `-w [output width]` -> Width of the output image (default: console width)  
- `-sv [save_path]` -> To choose a folder to save the file (default: desktop)  
- `-fn [filename]` -> To choose a file name (default: ascii+[random number])

### TO DO:
- [X] Add Image converter to ASCII.
- [X] Been able to adapt image/frame width.
- [X] Add Video converter to ASCII.
- [X] Add GIF converter to ASCII.
- [X] Convert images through urls.
- [X] Convert videos through youtube links.
- [X] Add CLI scripts.
- [ ] Add sound to the video player.
- [ ] Add color to the image converter. (Linux Only)
- [ ] Add color to the video/gif converters. (Linux Only)