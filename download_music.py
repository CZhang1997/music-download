import argparse
from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
from moviepy.editor import *

INPUT_DIR = "./songs"
VIDEO_DOWNLOAD_DIR = INPUT_DIR
AUDIO_DOWNLOAD_DIR = "./songs"
OUTPUT_DIR = "./converted_songs"

def convert_mp4_to_mp3(mp4_file, mp3_file):
    try:
        video = VideoFileClip(mp4_file)
        video.audio.write_audiofile(mp3_file)
    except Exception as e:
        print(f"Failed to convert {mp4_file} to MP3:", str(e))

def list_and_convert_mp4_to_mp3(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            mp4_file = os.path.join(directory, filename)
            mp3_file = os.path.join(OUTPUT_DIR, filename.replace(" ","").replace(".mp4", ".mp3"))
            convert_mp4_to_mp3(mp4_file, mp3_file)
            print(f"Converted {mp4_file} to {mp3_file}")
            os.remove(mp4_file)

def YoutubeVideoDownload(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_DOWNLOAD_DIR)
    except:
        print("Unable to download video at this time!")

    print("Video downloaded!")

def YoutubeAudioDownload(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio=True).first()

    try:
        audio_file = audio.download(AUDIO_DOWNLOAD_DIR)
        mp3_file = audio_file.replace(".mp4", ".mp3")  # Replace the extension
        convert_mp4_to_mp3(audio_file, mp3_file)
    except Exception as e:
        print("Failed to download or convert audio:", str(e))

    print("Audio was downloaded and converted successfully")

with open("./songs.txt", "r") as f:
    for song in f:
        if len(song.strip()) == 0:
            print("Skipping " + song)
            continue
        print(f"Downloading from {song}")
        YoutubeVideoDownload(song)

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

list_and_convert_mp4_to_mp3(INPUT_DIR)