# youtube-to-mp3
High quality YouTube video -> audio converter in CLI. Built using Python3. Embeds artist name and cover image into songs.

![app demo](https://i.ibb.co/frtwyXD/v3.gif)


## Setup & Installation
1. Clone this repo (either by SSH-ing or by direct downloading it)
2. Navigate to `youtube-to-mp3` folder which you have downloaded
3. [Create and activate  virtual environment for Python3](https://docs.python.org/3/library/venv.html) I named mine ytenv
4. The requirements are listed in `requirements.txt` You can install these easily by `pip install -r requirements.txt`
5. Install PyTube separately through `python -m pip install git+https://github.com/nficano/pytube` 
6. Run `python app.py` 

### Video Demo 
https://vimeo.com/479255729

## Notes
- The artist name field is required for the album art to be embedded properly
- PyTube has been observed to NOT work for a long period of time due to changes in YouTube's internal structure. Feel free to open any issues :)
