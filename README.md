# youtube-to-mp3
Python3 script to bulk download youtube links in .txt file to mp3 format. Embeds artist name and cover image into songs.

# Why I made this
I've found various solutions online (both web and CLI based) that allow you to download songs individually. These projects receive a youtube url as input and you get an mp3 audio as the output. This works, ...but I found myself repeating the same procedure multiple times, especially if you'd want to download multiple songs from different playlists. What if there was a way for me to download 20+ songs by just running a single script? This project solves exactly that!

# demo (youtube video)
demo using only 1 link in a text file.
[![video demo](demo.png)](https://youtu.be/4hJfliQ6g8w)


## Setup & Installation
1. Clone this repo (either by SSH-ing or by direct downloading it)
2. Navigate to `youtube-to-mp3` folder which you have downloaded
3. [Create and activate  virtual environment for Python3](https://docs.python.org/3/library/venv.html) I named mine ytenv
4. The requirements are listed in `requirements.txt` You can install these easily by `pip install -r requirements.txt`
5. Install PyTube separately through `python -m pip install git+https://github.com/nficano/pytube` 
6. Populate `links.txt` with the youtube video URLs line by line.
6. Run `python app.py` 


## Notes
- PyTube is always being updated and newer versions of this software are being released due to changes happening in YouTube's internal structure. Feel free to open any issues :)
