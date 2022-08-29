from pytube import YouTube
SAVE_PATH = "C:/Users/Hp/Documents/Test/"

link = "https://www.youtube.com/watch?v=QhjYUTYKGRo" 

try:
    yt = YouTube(link)
except:
    print("Error: Not able to find link")

title = yt.title
print(type(title))
print(yt.thumbnail_url)
videos = yt.streams.all()
for i in videos:
    print(i)
# print(yt.author)
# print(yt.views)
# print((yt.length)/60)
# print(yt.metadata)
# print(yt.streaming_data)

'''Listing all the streams of video'''
# lst = yt.streams.filter()
# for i in lst:
#     print(i)


'''Video'''
# print(yt.streams.filter(progressive = True).get_highest_resolution().itag)
# Itag = yt.streams.filter(progressive = True).get_highest_resolution().itag

# try:
#     yt.streams.get_by_itag(Itag).download(output_path = "C:/Users/Hp/Documents/Test/")
# except:
#     raise Exception    
# else:
#     print("video downloaded")

'''Audio'''
# print(yt.streams.filter(only_audio = True).get_audio_only().itag)
# Itag = yt.streams.filter(only_audio = True).get_audio_only().itag

# try:
#     yt.streams.get_by_itag(Itag).download(output_path = SAVE_PATH, filename = title +".mp3" )
# except:
#     raise Exception    
# else:
#     print("audio downloaded")
