from tkinter import *
from tkinter import ttk
import os

from MainRisker import FileToImages
from FramesToVideoNormal import ImagesToVideo
from MainBigSafe import FileToImagesBig
from FramesToVideoSafe import ImagesBigToVideo
from VideoDownloader import DLFromYt
from VideoToFileNormal import VideoToFileNormal
from VideoToFileBig import VideoToFileBig
from GetYtVideosName import get_channel_videos
from UploadeToYt import upload
from VideoDownloader import DLFromYt

CURRENT_PATH = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(CURRENT_PATH, "./config.ini")

l = {
    "Français": "fr", 
    "English": "en"
}

if not os.path.exists(CONFIG_PATH) or open(CONFIG_PATH, "r", encoding="utf8").read() not in [f"lang={l[i]}" for i in l.keys()]:
    w = Tk()
    w.title("Language")
    w.geometry("300x100")
    n = StringVar()
    def __save__():
        LANG = l[n.get()]
        open(CONFIG_PATH, "w", encoding="utf8").write(f"lang={LANG}")
        w.destroy()
    lcbb = ttk.Combobox(w, width = 30, textvariable = n)
    lcbb['values'] = list(l.keys())
    lcbb.place(x=50, y=20)
    lcbb.current(0)
    bouton=Button(w, text="Save", width = 27, command=__save__)
    bouton.place(x=50, y=50)
    w.mainloop()
else:
    LANG = open(CONFIG_PATH, "r", encoding="utf8").read().split("=")[-1]

lang = {
    "fr": {
        "url": "URL", 
        "api_key": "Clé d'API", 
        "file": "Fichier", 
        "setting": "Paramètre", 
        "slevel": "Sureté", 
        "slevel_value": [
            "Faible (plus de risque de corruption mais plus rapide)", 
            "Fort (Meme vitesse mais plus gros fichier vidéo)"
        ], 
        "extract": "extraire"
    }, 
    "en": {
        "url": "URL", 
        "api_key": "API key", 
        "file": "File", 
        "setting": "Setting", 
        "slevel": "Secure", 
        "slevel_value": [
            "Low (more risk of corruption but faster)", 
            "High (Same speed but bigger video file)"
        ], 
        "extract": "extract"
    }
}

lang = lang[LANG]

root = Tk()
root.geometry("800x500")

def __insert_list__(pos):
    urls = get_channel_videos(entreeUrl.get().strip())
    for i in range(len(urls)):
        liste.insert(i+1, urls[str(i+1)][1])
        print(urls[str(i+1)][1])
    liste.update()

lf = LabelFrame(root, text=lang["setting"])
lf.place(x=5, y=5, width=400, height=100)
label = Label(lf, text=lang["url"])
label.place(x=5, y=5)
url = StringVar() 
# url.set("https://www.youtube.com/channel/UCyj7svz9hL15ciYwrV_wpLg")
entreeUrl = Entry(lf, textvariable=url, width=50)
entreeUrl.place(x=60, y=5)
entreeUrl.bind("<FocusOut>", __insert_list__)
label = Label(lf, text=lang["api_key"])
label.place(x=5, y=30)
api = StringVar()
entreeApi = Entry(lf, textvariable=api, width=50)
entreeApi.place(x=60, y=30)
label = Label(lf, text=lang["slevel"])
label.place(x=5, y=55)
slevel = StringVar()
lcbb = ttk.Combobox(lf, width = 50, textvariable = slevel)
lcbb['values'] = lang["slevel_value"]
lcbb.place(x=60, y=55)
lcbb.current(0)

liste = Listbox(root, width=63, height=10)
liste.place(x=410, y=13)
btnextract=Button(root, text=lang["extract"], width=53, command=root.quit)
btnextract.place(x=410, y=180)





# channel_url = input('Enter a YouTube channel URL: ')

# urls = get_channel_videos(channel_url)
# ChoixCloud = int(input("Ajouter des fichiers (1), Extraire des fichiers(2), Afficher les fichiers (3) : "))
# if ChoixCloud == 1:
#     ChoixCompr = int(input(f"Niveau de sureté voulu ? : \n 1 : Faible (plus de risque de corruption mais plus rapide)\n2 : Fort (Meme vitesse mais plus gros fichier vidéo)\n"))

#     if ChoixCompr == 1:
#         fichiervoulue = str(input("Nom du fichier à convertir en vidéo (ne pas oublier l'extension) : "))
#         FileToImages(fichiervoulue)
        
#         video_name = fichiervoulue + '.mp4'
#         ImagesToVideo(video_name)
#         upload(video_name,video_name[:-4],'Compr1','22','','public')
        
#     if ChoixCompr == 2:
#         fichiervoulue = str(input("Nom du fichier a convertire en vidéo (sans oublier l'extension) : \n"))
#         FileToImagesBig(fichiervoulue)

#         video_name = fichiervoulue + '.mp4'
#         ImagesBigToVideo(video_name)
#         upload(video_name,video_name[:-4],'Compr2','22','','public')
#     for filename in os.listdir('./'):
#         if filename.endswith('.mp4'):
#             file_path = os.path.join('./', filename)
#             os.remove(file_path)
#             print(f"Deleted: {file_path}",end='\r')
# if ChoixCloud == 2:
#     for i in range(len(urls)):
#         print(i+1,urls[str(i+1)][1]+'\n')
#     ChoixVid = input("Selectionner le numéro associé au fichier a extraire : ")
#     urlDL = urls[ChoixVid][0]
#     print(urlDL)
#     DLFromYt(urlDL)
#     if urls[ChoixVid][3] == "Compr1":
#         nomVid = urls[ChoixVid][1].replace(".","") + ".mp4"
#         print(nomVid)
#         Vid = os.path.join('./videos',nomVid)
#         VideoToFileNormal(Vid,urls[ChoixVid][1])
        
#         os.remove(Vid)
#         print(f"Deleted: {file_path}",end='\r')

#     elif urls[ChoixVid][3] == "Compr2":
#         nomVid = urls[ChoixVid][1].replace(".","") + ".mp4"
#         Vid = os.path.join('./videos',nomVid)
#         VideoToFileBig(Vid,urls[ChoixVid][1])
#         os.remove(Vid)
#         print(f"Deleted: {file_path}",end='\r')
#     else:
#         print("Description invalide")

# if ChoixCloud == 3:
#     for i in range(len(urls)):
#         print(i+1,urls[str(i+1)][1]+'\n')
            




# bouton de sortie
# bouton=Button(root, text="Fermer", command=root.quit)
# bouton.place(x=5, y=5)

root.mainloop()