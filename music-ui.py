import tkinter as tk
import os
from tkinter import filedialog

import youtube_dl

current_directory = os.getcwd()
flag = 0
CONSOLE = "console: "
INSTRUCTION = 'Make sure you have the latest version for youtube-dl: \nsudo youtube-dl -U \n or \n pip3 install youtube-dl\n\nAfter that you can solve this problem by installing the missing ffmpeg. \nUbuntu and debian: sudo apt-get install ffmpeg \nmacOS: brew install ffmpeg \nWindows: choco install ffmpeg'

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        console_label.config(text=CONSOLE+msg)

def my_hook(d):
	global flag
	global console_label
    # global console_label

	if d['status'] == 'downloading':
		if(flag == 0):
			print('Source size: {0:.2f} MB' .format(d['total_bytes']/(1024*1024)))
			print('Downloading: ' + d['filename'])
            # consoleOutput= 'Source size: {0:.2f} MB' .format(d['total_bytes']/(1024*1024)) + '\nDownloading: ' + d['filename']
			flag = 1
		print('File Progress: {0:.2f}%' .format(d['downloaded_bytes'] / d['total_bytes']*100), end='\r')
		console_label.config(text=CONSOLE+ 'File Progress: {0:.2f}%' .format(d['downloaded_bytes'] / d['total_bytes']*100))
	if d['status'] == 'finished':
		flag = 0
		print('Done downloading, now converting ...')
		console_label.config(text=CONSOLE+'Done downloading')

def select_directory():
    """Open a file for editing."""
    new_directory = filedialog.askdirectory(initialdir=current_directory)
    print(new_directory)
    entry.delete(0, tk.END)
    entry.insert(0, new_directory)
    # print(label.cget("text"))
    

def button2_clicked():
    directory = entry.get()
    console_label.config(text=CONSOLE+'Starting to download')
    if not os.path.exists(directory):
        print("creating ", directory)
        os.makedirs(directory)

    ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio' : True,  # only keep the audio
    'audioformat' : "mp3",  # convert to mp3
    'outtmpl': directory +'/%(title)s.',    # name the file the ID of the video
    'noplaylist' : True,    # only download single song, not playlist
    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',
                        }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    }
    flag = 0
    # ydl_opts = {
	# 'outtmpl': directory + '\%(title)s.%(ext)s',
    # 'format': 'bestaudio/best',
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '320',
    # }],
    # 'logger': MyLogger(),
    # 'progress_hooks': [my_hook],
    # }
    urls = text_area.get("1.0", tk.END)
    songs = urls.splitlines()
    songs = [i for i in songs if i]
    # for url in urls.splitlines():
    #     print("url: ", url)
    # print(urls)
    # begin the download now
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(songs)

root = tk.Tk()
root.title("Youtube music downloader")
root.geometry("600x800")

label_frame = tk.Frame(root)
label_frame.pack()

path_label = tk.Label(label_frame, text="Download songs to:")
path_label.grid(row=0, column=0, sticky=tk.W)

entry = tk.Entry(label_frame, width=300, bg="white", fg="black")
entry.insert(0, current_directory)
entry.grid(row=0, column=1)
entry.focus()

links_label = tk.Label(root, text="Enter youtube urls below, separate by new line:")
links_label.pack()

text_area = tk.Text(root, bg="white")
text_area.pack()

# console_label = tk.Label(root, text="console: ")
# console_label.pack()

console_label = tk.Label(root, text=CONSOLE+INSTRUCTION)
console_label.pack()

button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

button1 = tk.Button(button_frame, text="Select download folder", command=select_directory)
button1.pack(side=tk.LEFT)

button2 = tk.Button(button_frame, text="Download", command=button2_clicked)
button2.pack(side=tk.LEFT, padx=20)

button_frame.pack(side=tk.BOTTOM, anchor="center")

root.mainloop()
