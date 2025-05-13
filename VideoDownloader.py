from pytubefix import YouTube

def DLFromYt(url):
    DOWNLOAD_FOLDER = "./videos"
    video = YouTube(url)
    videos = video.streams.all()
    for video in videos:
        if "720p" in str(video):
            try:
                print('video en cours de téléchargement')
                video.download(DOWNLOAD_FOLDER)
                break
            except:
                print("An error has occurred")
            print("Download is completed successfully")

    

