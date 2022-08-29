from pytube import Playlist
from pytube import YouTube
import logging
#Path where the files are downloadedd 
SAVE_PATH_FOR_MP4 = "D:/ASC/MUSIC/DOWNLOAD/VIDEO"
SAVE_PATH_FOR_MP3 = "D:/ASC/MUSIC/DOWNLOAD/AUDIO"

logger = logging.getLogger()
logging.basicConfig(level = logging.INFO,filename = 'Youtube_Downloader.log', format = '%(asctime)s:%(levelname)s:%(message)s')

'''Removing Unwanted characters from title'''
def remove_Unwanted_characters(title : str) -> str :
    title = title.replace('|',"")
    title = title.replace(':',"")
    title = title.replace('  '," ")
    return title 

'''Downloading Video'''        
def Downloading_yt_Video(link : str) -> None:
    try:
        yt = YouTube(link)
    except Exception as e:
        logger.exception(f"Link is invalid->\n {e}")    
    else:
        title = yt.title
        
        #Removing invalid characters from title 
        title = remove_Unwanted_characters(title)
        Itag = yt.streams.filter(progressive = True).get_highest_resolution().itag
        
        try:
            logger.info(f"Downloading: '{title}'")
            print(f"Downloading: '{title}'")
            yt.streams.get_by_itag(Itag).download(output_path = SAVE_PATH_FOR_MP4, filename = title + ".mp4")

        except Exception as e:
            logger.exception(f"Link is invalid->\n {e}") 
        else:
            logger.info(f"'{title}' downloaded")
            print(f"'{title}' downloaded")
            

'''Downloading Audio'''     
def Downloading_yt_Audio(link : str) -> None:
    try:
        yt = YouTube(link)
    except Exception as e:
        logger.exception(f"Link is invalid->\n {e}")
    else:   
        title = yt.title

        #Removing invalid characters from title 
        title = remove_Unwanted_characters(title)

        Itag = yt.streams.filter(only_audio = True).get_audio_only().itag
        
        try:
            logger.info(f"Downloading: '{title}'")
            print(f'Downloading: {title}')
            yt.streams.get_by_itag(Itag).download(output_path = SAVE_PATH_FOR_MP3, filename = title +".mp3" )
        except Exception as e:
            logger.exception(f"Link is invalid->\n {e}")  
        else:
            logger.info(f"'{title}' downloaded")
            print(f"'{title}' downloaded")
            

'''Downloading Audio files from Playlist'''
def Downloading_Playlist_in_mp3(link : str) -> None: #Pass the link of the Playlist to download
    try:
        #Creating Playlist Object
        p = Playlist(link)
    except Exception as e:
        logger.exception(f"Link is invalid->\n {e}")
    else:   
        if not p:
            logger.info("Playlist is Empty")
        else:
            for video in p.videos:
                title = video.title 
            
                #Removing invalid characters from title 
                title = remove_Unwanted_characters(title)
                
                #Filtering to get only the audio of the videos
                Itag = video.streams.filter(only_audio = True).get_audio_only().itag

                try:
                    logger.info(f"Downloading: '{title}'")
                    print(f'Downloading: {title}')
                    video.streams.get_by_itag(Itag).download(output_path = SAVE_PATH_FOR_MP3, filename = title + ".mp3")
                except Exception as e:
                    logger.exception(f"Link is invalid->\n {e}")     
                else:
                    logger.info(f"Audio of '{title}' downloaded")
                    print(f"Audio of '{title}' downloaded")


'''Downloading Video files from Playlist'''
def Downloading_Playlist_in_mp4(link : str) -> None: #Pass the link of the Playlist to download
    try:
        #Creating Playlist Object
        p = Playlist(link)
    except Exception as e:
        logger.exception(f"Link is invalid->\n {e}")
    else:   
        if not p:
            logger.info("Playlist is Empty")
        else:
            for video in p.videos:
                title = video.title 
            
                #Removing invalid characters from title 
                title = remove_Unwanted_characters(title)

                # print(video.streams.filter(progressive = True).get_highest_resolution().itag)
                Itag = video.streams.filter(progressive = True).get_highest_resolution().itag

                try:
                    logger.info(f"Downloading: '{title}'")
                    print(f'Downloading: {title}')
                    video.streams.get_by_itag(Itag).download(output_path = SAVE_PATH_FOR_MP4, filename = title+".mp4")
                except Exception as e:
                    logger.exception(f"Link is invalid->\n {e}")    
                else:
                    print(f"'{title}' downloaded")
                    logger.info(f"'{title}' downloaded")


'''Main Function'''
if __name__ == "__main__":

    print("*******************")
    print("Enter 1: Download a Video\nEnter 2: Download an Audio\nEnter 3: Download a Video Playlist\nEnter 4: Download an Audio Playlist\n")
    ch = int(input("Your choice -> "))

    link = input("Enter the link of youtube video or playlist->")
   
    if ch == 1:
        Downloading_yt_Video(link)
    elif ch == 2:
        Downloading_yt_Audio(link)
    elif ch == 3:
        Downloading_Playlist_in_mp4(link)
    elif ch == 4:
        Downloading_Playlist_in_mp3(link)
    else:
        print("Invalid Choice")