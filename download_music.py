
from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
                       'key': 'FFmpegExtractAudio',
                       'preferredcodec': 'mp3',
                       'preferredquality': '192',
                       }],
}

options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3
  'outtmpl': '%(title)s.',    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
  'postprocessors': [{
                       'key': 'FFmpegExtractAudio',
                       'preferredcodec': 'mp3',
                       'preferredquality': '192',
                       }],
}

with youtube_dl.YoutubeDL(options) as ydl:
    with open("../songs.txt", "r") as f:
        for song in f:
            ydl.download([song])



#        for x in range(24):
 #           if(x > 4 and x != 6):
  #              url = "https://www.youtube.com/watch?v=vy0bF50WE4c&list=PLoZkshdc-b21aOefm5prCcr5ArDQ8zSHr&index={}".format(x+2)
   #             print(url)
                #ydl.download([url])
#ydl.download(['https://www.youtube.com/watch?v=HHcZXcggzJA'])
