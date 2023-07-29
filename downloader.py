from pytube import YouTube
import sys
import requests
from bs4 import BeautifulSoup


def Download(link):
    ytObj = YouTube(link)
    print(f"downloading video from url: {link}")
    ytObj = ytObj.streams.get_highest_resolution()
    try:
        ytObj.download()
    except ():
        print("downloader alert")
    print("get scraped")


def helpmessage():
    print(" Welcome to youtube downloader")
    print("""
 If you are trying to download a single video,
 run the script with the first argument being video ,
 and the second one being the link.
 If you are trying to download a whole playlist,
 the first argument should be playlist ,
 the second should be the playlist link,
 and the third one should be the number of videos in the playlist
 (or the first N videos to be downloaded).
 make sure it is either public or unlisted , before using this script.
 to display this message, use -h""")


def scrape_vids_from_url(url, num):
    content = ""
    vids = []
    page = requests.get(url)
    content = str(BeautifulSoup(page.content, "html.parser"))
    start = 0
    print("alive")
    for i in range(num):
        content = content[start:]
        pos = content.find("watch?v=")
        end = content[pos:].find("\\")
        sliced = content[pos:pos + end]
        result = f"https://www.youtube.com/{sliced}"
        vids.append(result)
        start = pos + end
    print(vids)
    return vids


if __name__ == "__main__":
    if (sys.argv.__len__() == 1):
        print("insufficient arguments , try -h for help")
        exit()
    if str(sys.argv[1]) == "playlist":
        playlist = str(sys.argv[2])
        num = int(sys.argv[3])
        videoList = scrape_vids_from_url(playlist, num)
        for video in videoList:
            Download(video)
        exit()
    if str(sys.argv[1]) == "video":
        link = str(sys.argv[2])
        Download(link)
    if str(sys.argv[1]) == "-h":
        helpmessage()
