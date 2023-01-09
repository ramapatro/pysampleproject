from pytube import YouTube
yt = YouTube('https://youtu.be/RU8mQmD-U88')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('./videos')
