from pytube import YouTube
import sys


def Download(link):
    ytObj = YouTube(link)

    ytObj = ytObj.streams.get_highest_resolution()
    try:
        ytObj.download()
    except ():
        print("downloader alert")
    print("get scraped")


def scrape_playlist_link():
    print("i am incomplete")


def scrape_vids_from_url():
    print("i am incomplete")


if __name__ == "__main__":
    if str(sys.argv[1]) == "playlist":
        playlistName = str(sys.argv[2])
        playlist = scrape_playlist_link(playlistName)
        videoList = scrape_vids_from_url(playlist)
        for video in videoList:
            Download(video)
    print(str(sys.argv))
    link = str(sys.argv[1])
    Download(link)
