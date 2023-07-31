#!/usr/bin/env python
from pytube import YouTube, Playlist
import sys
import requests
from bs4 import BeautifulSoup
import os


def Download(link, isAudio, folderName="Downloads"):
    ytObj = YouTube(link)
    if isAudio is False:
        print(f"downloading video from url: {link}")
        ytObj = ytObj.streams.get_highest_resolution()
        try:
            ytObj.download(output_path=folderName)
        except Exception:
            print("downloader alert")
    else:
        print(f"downloading audio from url: {link}")
        ytObj = ytObj.streams.get_audio_only()
        try:
            path = ytObj.download(output_path=folderName)
            newName = path
            os.rename(path, newName)
        except Exception:
            print("downloader alert")
    print("get scraped")


def helpmessage():
    print(" Welcome to youtube downloader")
    print("""
 If you are trying to download a single video,
 run the script with the first argument being video ,
 and the second one being the link.
 To download a single audio-only file(from a video) ,
 the first argument should be audio, and the second one should be the link.
 If you are trying to download a whole playlist,
 the first argument should be playlist ,
 the second should be the playlist link,
 and the third one should be the number of videos you wish to download.
 If a third argument isn't provided,the entire playlist will be downloaded.
 Make sure it is either public or unlisted , before using this script.
 To download only the audio portions from a playlist , use tracklist instead,
 with the rest of the arguments being the same as with a regular playlist.
 To display this message, use -h""")


def scrape_vids_from_url(url, num):
    content = ""
    vids = []
    page = requests.get(url)
    content = str(BeautifulSoup(page.content, "html.parser"))
    start = 0
    for i in range(num):
        content = content[start:]
        pos = content.find("watch?v=")
        end = content[pos:].find("\\")
        sliced = content[pos:pos + end]
        result = f"https://www.youtube.com/{sliced}"
        vids.append(result)
        start = pos + end
    return vids


if __name__ == "__main__":
    if (sys.argv.__len__() == 1):
        print("insufficient arguments , try -h for help")
        exit()
    if str(sys.argv[1]) == "playlist":
        playlist = str(sys.argv[2])
        plobject = Playlist(playlist)
        playlistName = plobject.title
        playlistName = os.getcwd() + f"/{playlistName}"
        try:
            os.mkdir(playlistName)
        except Exception:
            pass
        num = plobject.length
        if len(sys.argv) == 4:
            num = int(sys.argv[3])
        videoList = scrape_vids_from_url(playlist, num)
        for video in videoList:
            Download(video, False, playlistName)
        exit()
    if str(sys.argv[1]) == "tracklist":
        playlist = str(sys.argv[2])
        plobject = Playlist(playlist)
        playlistName = plobject.title
        playlistName = os.getcwd() + f"/{playlistName}"
        try:
            os.mkdir(playlistName)
        except Exception:
            pass
        num = plobject.length
        if len(sys.argv) == 4:
            num = int(sys.argv[3])
        audioList = scrape_vids_from_url(playlist, num)
        for track in audioList:
            Download(track, True, playlistName)
        exit()
    try:
        os.mkdir("Downloads")
    except Exception:
        pass
    if str(sys.argv[1]) == "video":
        link = str(sys.argv[2])
        Download(link, False)
        exit()
    if str(sys.argv[1]) == "audio":
        link = str(sys.argv[2])
        Download(link, True)
        exit()
    if str(sys.argv[1]) == "-h":
        helpmessage()
