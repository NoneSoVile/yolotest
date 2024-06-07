from pytube import YouTube
import sys
if len(sys.argv) <= 1:
    print("input the url of video")
    exit()
    
yt = YouTube(sys.argv[1])

print(yt.title)
#print(yt.streams)
print('=======================filter==========')
videolist = yt.streams.filter(progressive=True, file_extension='mp4', res="360p")
num = videolist.count()


print("choice : ", num)
if num == 1:
    video = videolist.first()
    video.download('video')
else:
    print('too much choice, ajust the filter to reduce the streams')
#print(yt.streams.filter(progressive=True, file_extension='mp4'))

#stream = yt.streams.get_by_itag(18)
#stream.download('video')