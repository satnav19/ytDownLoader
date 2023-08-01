# ytDownloader
ytDownloader is a Python script for downloading YouTube videos and playlists, with or without sound.

## Installation
Needed packages are in the requirements.txt file.

To use as a script, use `chmod +x downloader.py`

## Usage
`./downloader.py [video|audio|tracklist|playlist link]  [video/playlist link] `
 
If using a playlist, make sure the playlist is either unlisted, or public. 

Options are:
  - video: download a video with audio
  - audio: download a video without audio
  - tracklist: download videos from a playlist without audio
  - playlist: download videos from a playlist with audio


An optional third argument is `[Number of vids to be downloaded]` , only relevent when downloading a playlist.

If the third argument isn't provided, all videos in the given playlist will be downloaded.
To display this message, use `-h` or `-help`


