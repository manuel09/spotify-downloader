# importing modules

import webbrowser
import time
import requests
from bs4 import BeautifulSoup
import json
import yt_dlp
import os
from idm import IDMan
import imp

# functions

def ytmusic():
    song_name = input('Enter the song name or song url\n').replace(" ","%")
    url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&q="+song_name+"&key=AIzaSyBo6h-t4F2M_MahpexHJPSS4wiycIm638I&maxResults=5"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')

    a = str(soup)
    b = json.loads(a)
    video_id = (b['items'][0]['id']['videoId'])
    video_url = (str("https://www.youtube.com/watch?v="+video_id))
    video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{''+video_info['title']}.mp3"
    options={
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'keepvideo':False,
        'writethumbnail': True,
        'key': 'EmbedThumbnail',
        'outtmpl': "/canzoni/%(title)s-%(id)s.%(ext)s"
    }
      
    with yt_dlp.YoutubeDL(options) as ydlp:
        ydlp.download([video_info['webpage_url']])

def ytvideo():
    song_name = input('Enter the video name or video url\n').replace(" ","%")
    url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&q="+song_name+"&key=AIzaSyBo6h-t4F2M_MahpexHJPSS4wiycIm638I&maxResults=5"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')

    a = str(soup)
    b = json.loads(a)
    video_id = (b['items'][0]['id']['videoId'])
    video_url = (str("https://www.youtube.com/watch?v="+video_id))
    video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{''+video_info['title']}.mp4"
    options={
        'outtmpl':"/video/%(title)s-%(id)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(options) as ydlp:
        ydlp.download([video_info['webpage_url']])

def idmdownload():
    downloader = IDMan()

    url = input('Enter url of file\n')

    downloader.download(url, r"c:/DOWNLOADS", output=None, referrer=None, cookie=None, postData=None, user=None, password=None, confirm = False, lflag = None, clip=False)

# logics

while True:
    options = input('Choose:\n1. Yt Video \n2. Yt Audio Only \n3. Idm download with direct link\n')
    if options == 1 or options == "1":
        ytvideo()
    elif options == 2 or options == "2":
        ytmusic()
    elif options == 3 or options == "3":
        idmdownload()
    restatus = input('Do you want more download y/n\n')
    if "y" in restatus:
        pass
    elif "n" in restatus:
        break



input('enter to exit')
