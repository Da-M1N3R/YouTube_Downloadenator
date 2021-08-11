import tkinter as tk
from pytube import YouTube
from moviepy.editor import *
import os
import urllib.request

root = tk.Tk()
root.title("YouTube Video Downloadenator")

# Grid management
r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
c0, c1, c2, c3, c4, c5, c6 = 0, 1, 2, 3, 4, 5, 6
cspan = 4

# GUI customization
tk.Label(root, text = "YouTube Downloadenator", font = "arial 20 bold").grid(column=c1, row=r0, columnspan=cspan)
tk.Label(root, text = 'Paste Link Here:', font = 'arial 10 bold').grid(column=c1, row=r1, columnspan=cspan)

# Enter YT link
link = tk.StringVar()
link_enter = tk.Entry(root, width = 90, textvariable = link).grid(column=c1, row=r2, columnspan=cspan)

# Download function
# Download different resolution: 144p, 240p, 360p, 480p, 720p, 1080p, 1440p, 2160p
def download144p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(progressive = True, res = "144p")
    print("Checking 144p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '144p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download()
    print('DOWNLOADED 144p')
    return tk.Label(root, text = 'DOWNLOADED 144p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

def download240p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(progressive = True, res = "240p")
    print("Checking 240p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '240p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download()
    print('DOWNLOADED 240p')
    return tk.Label(root, text = 'DOWNLOADED 240p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

def download360p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(progressive = True, res = "360p")
    print("Checking 360p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '360p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download()
    print('DOWNLOADED 360p')
    return tk.Label(root, text = 'DOWNLOADED 360p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

def download480p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(progressive = True, res = "480p")
    print("Checking 480p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '480p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download()
    print('DOWNLOADED 480p')
    return tk.Label(root, text = 'DOWNLOADED 480p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

def download720p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(progressive = True, res = "720p")
    print("Checking 720p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '720p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download()
    print('DOWNLOADED 720p')
    return tk.Label(root, text = 'DOWNLOADED 720p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

# By using DASH method (For High Quality Video)
def combine_video_audio(video_file, audio_file, new_filename, save):
    videoclip = VideoFileClip(video_file)
    audioclip = AudioFileClip(audio_file)
    print("Setting audio into video file...")
    videoclip = videoclip.set_audio(audioclip)
    if save:
        videoclip.write_videofile(new_filename)
    print("Download Complete.")

def download1080p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(res = "1080p", type = "video")
    print("Checking 1080p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '1080p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download(filename = "YT_downloadenator_vid.mp4")
    audio = ytv.streams.filter(type = "audio")
    print("Available audio...")
    print(audio)
    audio = audio[0]
    audio.download(filename = "YT_downloadenator_aud.mp4")
    combine_video_audio("YT_downloadenator_vid.mp4", "YT_downloadenator_aud.mp4", "output.mp4", True)
    os.remove("YT_downloadenator_vid.mp4")
    os.remove("YT_downloadenator_aud.mp4")
    print('DOWNLOADED 1080p')
    return tk.Label(root, text = 'DOWNLOADED 1080p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

def download1440p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(res = "1440p", type = "video")
    print("Checking 1440p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '1440p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download(filename = "YT_downloadenator_vid.mp4")
    audio = ytv.streams.filter(type = "audio")
    print("Available audio...")
    print(audio)
    audio = audio[0]
    audio.download(filename = "YT_downloadenator_aud.mp4")
    combine_video_audio("YT_downloadenator_vid.mp4", "YT_downloadenator_aud.mp4", "output.mp4", True)
    os.remove("YT_downloadenator_vid.mp4")
    os.remove("YT_downloadenator_aud.mp4")
    print('DOWNLOADED 1440p')
    return tk.Label(root, text = 'DOWNLOADED 1440p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

def download2160p():
    ytv = YouTube(str(link.get()))
    video = ytv.streams.filter(res = "2160p", type = "video")
    print("Checking 2160p...")
    print("Available video...")
    print(video)
    if len(video) == 0:
        return tk.Label(root, text = '2160p UNAVAILABLE', font = 'arial 15', fg = 'red').grid(column=c1, row=r6, columnspan=cspan)
    video = video[0]
    video.download(filename = "YT_downloadenator_vid.mp4")
    audio = ytv.streams.filter(type = "audio")
    print("Available audio...")
    print(audio)
    audio = audio[0]
    audio.download(filename = "YT_downloadenator_aud.mp4")
    combine_video_audio("YT_downloadenator_vid.mp4", "YT_downloadenator_aud.mp4", "output.mp4", True)
    os.remove("YT_downloadenator_vid.mp4")
    os.remove("YT_downloadenator_aud.mp4")
    print('DOWNLOADED 2160p')
    return tk.Label(root, text = 'DOWNLOADED 2160p', font = 'arial 15').grid(column=c1, row=r6, columnspan=cspan)

# Download thumbnail
def get_thumbnail():
    print("YouTube video Link: ")
    print(ytv.thumbnail_url)
    urllib.request.urlretrieve(ytv.thumbnail_url, "thumbnail.png")
    print("DOWNLOADED video thumbnail.")
    return tk.Label(root, text = 'DOWNLOADED thumbnail', font = 'arial 15').grid(column=c2, row=r12, columnspan=3)

# Get details of video
def about_ytv():
    global ytv
    ytv = YouTube(str(link.get()))
    # Title
    tk.Label(root, text = 'Title:', font = 'arial 15').grid(column=c1, row=r7)
    tk.Label(root, text = ytv.title, font = 'arial 15').grid(column=c2, row=r7, columnspan=3)
    # Views
    tk.Label(root, text = 'Views:', font = 'arial 15').grid(column=c1, row=r8)
    tk.Label(root, text = ytv.views, font = 'arial 15').grid(column=c2, row=r8, columnspan=3)
    # Rating
    tk.Label(root, text = 'Rating:', font = 'arial 15').grid(column=c1, row=r9)
    tk.Label(root, text = str(ytv.rating) + " / 5", font = 'arial 15').grid(column=c2, row=r9, columnspan=3)
    # Length
    tk.Label(root, text = 'Length:', font = 'arial 15').grid(column=c1, row=r10)
    tk.Label(root, text = str(ytv.length) + " seconds", font = 'arial 15').grid(column=c2, row=r10, columnspan=3)
    # Thumbnail
    tk.Label(root, text = 'Thumbnail:', font = 'arial 15').grid(column=c1, row=r11)
    tk.Button(root, text = "Get Thumbnail", font = 'arial 15 bold', bg = 'blue', command = get_thumbnail).grid(column=c2, row=r11, columnspan=3)
    '''
    # Description
    tk.Label(root, text = 'Description:', font = 'arial 15').grid(column=c1, row=r11)
    tk.Label(root, text = ytv.description, font = 'arial 15').grid(column=c2, row=r11, columnspan=3)
    '''

# Download button
tk.Button(root, text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'pink', state = 'disable').grid(column=c1, row=r3, columnspan=2)
# About button
tk.Button(root, text = 'ABOUT', font = 'arial 15 bold', bg = 'light blue', padx = 2, command = about_ytv).grid(column=c3, row=r3, columnspan=2)

# Different resolutions
tk.Button(root, width = 5, text = "144p", font = "arial 20 bold", bg = "red", padx = 2, command = download144p).grid(column=c1, row=r4)
tk.Button(root, width = 5, text = "240p", font = "arial 20 bold", bg = "red", padx = 2, command = download240p).grid(column=c2, row=r4)
tk.Button(root, width = 5, text = "360p", font = "arial 20 bold", bg = "red", padx = 2, command = download360p).grid(column=c3, row=r4)
tk.Button(root, width = 5, text = "480p", font = "arial 20 bold", bg = "red", padx = 2, command = download480p).grid(column=c4, row=r4)
tk.Button(root, width = 5, text = "720p", font = "arial 20 bold", bg = "red", padx = 2, command = download720p).grid(column=c1, row=r5)
tk.Button(root, width = 5, text = "1080p", font = "arial 20 bold", bg = "red", padx = 2, command = download1080p).grid(column=c2, row=r5)
tk.Button(root, width = 5, text = "1440p", font = "arial 20 bold", bg = "red", padx = 2, command = download1440p).grid(column=c3, row=r5)
tk.Button(root, width = 5, text = "2160p", font = "arial 20 bold", bg = "red", padx = 2, command = download2160p).grid(column=c4, row=r5)

root.geometry("1000x500")
root.mainloop()
