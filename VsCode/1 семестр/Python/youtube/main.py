from pytube import YouTube

url = 'https://youtu.be/WahaanhcKwo?si=8DO825icohkZ5aWI'

yt = YouTube(url)
print(f'Download video {yt.title!r}: {url}')

streams = yt.streams\
    .filter(progressive=True, file_extension='mp4', resolution='720p')\
    .order_by('resolution')

video = streams[-1]
print('Stream url:', video.url)
video.download()