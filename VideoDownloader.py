from pytubefix import YouTube

def DLFromYt(url):
    DOWNLOAD_FOLDER = "./videos"
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    try:
        print('video en cours de téléchargement')
        video.download(DOWNLOAD_FOLDER)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

