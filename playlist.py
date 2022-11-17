from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

playlisturl = "https://www.youtube.com/watch?v=giZu291ISRg&list=PLnbOFYlamFHAjtt8taeQ1dX00eA2B5O0b"
playlist = Playlist(playlisturl)

#prints each video url, which is the same as iterating through playlist.video_urls
for url in playlist:
    print(url)
#prints address of each YouTube object in the playlist
for vid in playlist.videos:
    print(vid)

for url in playlist:
   YouTube(url).streams.filter(only_audio=True).first().download("./songs")
   
# for url in playlist:
#    YouTube(url).streams.first().download('/Users/mklaben21/Desktop/custom songs')