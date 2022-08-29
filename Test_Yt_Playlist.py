from pytube import Playlist

SAVE_PATH = "C:/Users/Hp/Documents/Test/"
# p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

#Creating a playlist from a link
p = Playlist('https://www.youtube.com/watch?v=xQMMBANbcdQ&list=PLG6-gcUPBICX9UmX3JZYq05xhQIKe6WEl')

# print(f'Downloading: {p.title}')
# Downloading: Python Tutorial for Beginers (For Absolute Beginners)
for video in p.videos:
    # print("**************************")
    # lst = video.streams.filter()
    # for i in lst:
    #     print(i)
    # print(video.streams.filter(only_audio = True).get_audio_only().itag)
    title = video.title 
    
    #Removing invalid characters from title 
    title = title.replace('|',"")
    title = title.replace(':',"")
    title = title.replace('  '," ")

    Itag = video.streams.filter(only_audio = True).get_audio_only().itag

    try:
        video.streams.get_by_itag(Itag).download(output_path = SAVE_PATH, filename = title + ".mp3")
    except:
        raise Exception    
    else:
        print(f"{title} audio downloaded")




# #Only urls of video:
# print(len(p.video_urls))
# for url in p.video_urls[:len(p.video_urls)]:
#      print(url)