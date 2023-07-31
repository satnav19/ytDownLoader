 Welcome to my youtube downloader !
 I’ve added a shebang to the top of the .py file , so if you allow it to execute using chmod +x downloader.py , you can run it directly.
 All required Python libraries are in requirements.txt , but not all of those are      needed :) 
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
 To display this message, use -h


