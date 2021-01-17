#!/usr/bin/env python

from pytube import YouTube
import os
from moviepy.editor import *
import eyed3
import requests

#--------- DOWNLOADING AUDIO FROM YOUTUBE -----------------
# user inputs



path1 = '.'

# Open the file with read only permit
g = open('links.txt')
# use readline() to read the first line 
line = g.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
while line:
	print(line)

	# downloading video using pytube
	yt = YouTube(line)
	artist_name = yt.streams[0].title
	# now we have a YouTube object called yt
	# printing the title of the video to terminal screen
	song_name = yt.title
	print(song_name)
	img_id = yt.thumbnail_url

	# see available media formats
	yt.streams.all()
	# getting the first stream option
	stream = yt.streams.first()
	# downloading video to path2
	path2 = stream.download(path1)
	mp4_file = path2
	# creating a path for mp3 file
	path3 = path1 + "/" +  song_name + ".mp3"
	mp3_file = path3

	# conversion from mp4 to mp3
	videoclip = VideoFileClip(mp4_file) # create a videoclip object
	audioclip = videoclip.audio # get the audio object from mp4 file
	audioclip.write_audiofile(mp3_file) # save the audio of mp4 into an mp3 file
	audioclip.close()
	videoclip.close()

	os.remove(path2)

	#--------- DOWNLOADING YOUTUBE THUMBNAIL IMAGE -----------------

	# message confirming that the img download process has started
	print('Importing youtube thumbnail...')

	url = img_id
	r = requests.get(url)

	# assigning a path for the temporary image file
	# (it's going to get deleted after embed onto mp3)
	path4 = path1 + "/img" + ".jpg"

	with open(path4, 'wb') as f:
	    f.write(r.content)

	# retrieving HTTP meta-data
	print(r.status_code)
	print(r.headers['content-type'])
	print(r.encoding)

	#--------- EMBEDDING THUMBNAIL IMG ONTO MP3 FILE -----------------

	audiofile = eyed3.load(mp3_file)
	if (audiofile.tag == None):
	    audiofile.initTag()

	audiofile.tag.images.set(3, open(path4,'rb').read(), 'image/jpeg')
	audiofile.tag.album_artist = artist_name
	audiofile.tag.save()

	# deleting the thumbnail as it's not needed anymore
	os.remove(path4)
	print(song_name + " downloaded successfully :)")
	# reading next line
	line = g.readline()

f.close()

