#Download Youtube Video

from pytube import YouTube

url=input('Enter Video Link: ')
my_video=YouTube(url)
print('Video Title')
print(my_video.title)

print('Thumbnail Image')
print(my_video.thumbnail_url)

print('Download Video')
my_video=my_video.streams.get_highest_resolution()

#my_video=my_video.streams.first()

my_video.download()

'''
for stream in my_video.streams:
    print(stream)
'''
   
