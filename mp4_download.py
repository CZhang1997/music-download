import argparse
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
from moviepy.editor import *

VIDEO_DOWNLOAD_DIR = "./videos"


def YoutubeVideoDownload(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_DOWNLOAD_DIR)
    except:
        print("Unable to download video at this time!")

    print("Video downloaded!")


with open("./movie.txt", "r") as f:
    for song in f:
        if len(song.strip()) == 0:
            print("Skipping " + song)
            continue
        if "youtube.com" not in song:
            song = "https://www.youtube.com"+song

        print(f"Downloading from {song}")
        YoutubeVideoDownload(song)
