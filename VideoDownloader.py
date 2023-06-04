from pytube import YouTube

DOWNLOAD_FOLDER = "./videos"
url = str(input('Saisir url a convertire en fichier : ' ))

def dl(url):
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    try:
        print('video en cours de téléchargement')
        video.download(DOWNLOAD_FOLDER)
    except:
        print("An error has occurred")
    print("Download is completed successfully")

dl(url)