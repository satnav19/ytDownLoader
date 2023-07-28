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


if __name__ == "__main__":

    print(str(sys.argv))
    link = str(sys.argv[1])
    Download(link)
