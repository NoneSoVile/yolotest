from pytube import YouTube
import os
import subprocess

# URL of the YouTube video
video_url = 'https://www.youtube.com/shorts/M5KK-TOEaOA'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution video stream that contains only video (no audio)
video_stream = yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()

# Get the highest quality audio stream
audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# Download the video and audio streams
video_path = video_stream.download(filename='video/video.mp4')
audio_path = audio_stream.download(filename='video/audio.mp4')

# Combine the video and audio streams using ffmpeg
output_path = 'video/final_output.mp4'
subprocess.run([
    'ffmpeg',
    '-i', video_path,
    '-i', audio_path,
    '-c:v', 'copy',
    '-c:a', 'aac',
    '-strict', 'experimental',
    output_path
])

# Remove the separate video and audio files if you no longer need them
os.remove(video_path)
os.remove(audio_path)

print(f'Video saved as {output_path}')