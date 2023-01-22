import os
from pytube import YouTube

filename = "links.txt"
destination = "output"

isExist = os.path.exists(destination)
if not isExist:
   os.makedirs(destination)

with open(filename, 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        yt = YouTube(line)
        video = max(yt.streams.filter(only_audio=True), key=lambda x: int(x.abr[:-4]))
        print(video.abr)
        out_file = video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")