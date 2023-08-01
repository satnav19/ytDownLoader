#!/usr/bin/env python
from pytube import YouTube, Playlist, exceptions
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
        except exceptions.PytubeError:
            print("downloader alert")
    else:
        print(f"downloading audio from url: {link}")
        ytObj = ytObj.streams.get_audio_only()
        try:
            path = ytObj.download(output_path=folderName)
            newName = path
            os.rename(path, newName)
        except OSError:
            print("downloader alert")
    print("get scraped")


def helpmessage():
    file = open("README.md")
    print(file.read())


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


def Dtracklist(tracklist, num, tlobject):
    tracklistName = tlobject.title
    tracklistName = os.getcwd() + f"/{tracklistName}"
    try:
        os.mkdir(tracklistName)
    except FileExistsError:
        pass
    audioList = scrape_vids_from_url(tracklist, num)
    for track in audioList:
        Download(track, True, tracklistName)
    exit()


def Dplaylist(playlist, num, plobject):
    playlistName = plobject.title
    playlistName = os.getcwd() + f"/{playlistName}"
    try:
        os.mkdir(playlistName)
    except Exception:
        pass
    videoList = scrape_vids_from_url(playlist, num)
    for video in videoList:
        Download(video, False, playlistName)
    exit()


def openDefaultDir():
    try:
        os.mkdir("Downloads")
    except FileExistsError:
        pass


if __name__ == "__main__":
    if (sys.argv.__len__() == 1):
        print("insufficient arguments , try -h for help")
        exit()
    if str(sys.argv[1]) == "playlist":
        playlist = str(sys.argv[2])
        plobject = Playlist(playlist)
        num = plobject.length
        if len(sys.argv) == 4:
            num = int(sys.argv[3])
        Dplaylist(playlist, num, plobject)
    if str(sys.argv[1]) == "tracklist":
        tracklist = str(sys.argv[2])
        tlobject = Playlist(tracklist)
        num = tlobject.length
        if len(sys.argv) == 4:
            num = int(sys.argv[3])
        Dtracklist(tracklist, num, tlobject)
    openDefaultDir()
    if str(sys.argv[1]) == "video":
        link = str(sys.argv[2])
        Download(link, False)
        exit()
    if str(sys.argv[1]) == "audio":
        link = str(sys.argv[2])
        Download(link, True)
        exit()
    if str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "-help":
        helpmessage()
