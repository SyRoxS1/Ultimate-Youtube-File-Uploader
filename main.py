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
from RotateForShort import Rotate
import os

if __name__ == '__main__':
    PremierChoix = int(input("Vidéo -> Fichier (1)\nFichier -> Vidéo (2)\nYoutubeAsAcloud (beta)(3): "))
    if PremierChoix == 1:
        url = str(input('Saisir url a convertire en fichier : ' ))
        DLFromYt(url)

        TypeVideo = int(input("Saisire le type de vidéo : (1) : Normale (2) : Insecure : "))
        if TypeVideo == 1:
            nomfichier = str('./videos/'+ input("Saisir le nom de la vidéo télécharger (sans l'extension) : ")+'.mp4')
            print(nomfichier)
            final = str(input("Saisir le nom du fichier a recréer a partire de la vidéo (ne pas oublier l'extension) : "))
            VideoToFileNormal(nomfichier,final)

        if TypeVideo == 2:
            nomfichier = str('./videos/'+ input("Saisir le nom de la vidéo télécharger (sans l'extension): ")+'.mp4')
            print(nomfichier)
            final = str(input("Saisir le nom du fichier a recréer a partire de la vidéo (ne pas oublier l'extension .zip (ou autres)) : "))
            VideoToFileBig(nomfichier,final)
        
    if PremierChoix == 2:
        ChoixCompr = int(input(f"Niveau de sureté voulu ? : \n 1 : Faible (plus de risque de corruption mais plus rapide)\n2 : Fort (Meme vitesse mais plus gros fichier vidéo)\n"))
    
        if ChoixCompr == 1:
            ChoixInclinaison = int(input("Horizontal (1) ou Vertical (2) : "))

            if ChoixInclinaison == 1:
                fichiervoulue = str(input("Nom du fichier à convertir en vidéo (ne pas oublier l'extension) : "))
                FileToImages(fichiervoulue)
                video_name = fichiervoulue + '.mp4'
                ImagesToVideo(video_name)

            if ChoixInclinaison == 2:
                fichiervoulue = str(input("Nom du fichier à convertir en vidéo (ne pas oublier l'extension) : "))
                FileToImages(fichiervoulue)
                Rotate()
                video_name = fichiervoulue + '.mp4'
                ImagesToVideo(video_name)


        if ChoixCompr == 2:
            fichiervoulue = str(input("Nom du fichier a convertire en vidéo (sans oublier l'extension) : \n"))
            FileToImagesBig(fichiervoulue)

            video_name = fichiervoulue + '.mp4'
            ImagesBigToVideo(video_name)

    if PremierChoix == 3:
        channel_url = input('Enter a YouTube channel URL: ')
        
        urls = get_channel_videos(channel_url)
        ChoixCloud = int(input("Ajouter des fichiers (1), Extraire des fichiers(2), Afficher les fichiers (3) : "))
        if ChoixCloud == 1:
            ChoixCompr = int(input(f"Niveau de sureté voulu ? : \n 1 : Faible (plus de risque de corruption mais plus rapide)\n2 : Fort (Meme vitesse mais plus gros fichier vidéo)\n"))
    
            if ChoixCompr == 1:
                fichiervoulue = str(input("Nom du fichier à convertir en vidéo (ne pas oublier l'extension) : "))
                FileToImages(fichiervoulue)
                
                video_name = fichiervoulue + '.mp4'
                ImagesToVideo(video_name)
                upload(video_name,fichiervoulue,'Compr1','22','','public')
                
            if ChoixCompr == 2:
                fichiervoulue = str(input("Nom du fichier a convertire en vidéo (sans oublier l'extension) : \n"))
                FileToImagesBig(fichiervoulue)
    
                video_name = fichiervoulue + '.mp4'
                ImagesBigToVideo(video_name)
                upload(video_name,fichiervoulue,'Compr2','22','','public')
            for filename in os.listdir('./'):
                if filename.endswith('.mp4'):
                    file_path = os.path.join('./', filename)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}",end='\r')
        if ChoixCloud == 2:
            for i in range(len(urls)):
                print(i+1,urls[str(i+1)][1]+'\n')
            ChoixVid = input("Selectionner le numéro associé au fichier a extraire : ")
            urlDL = urls[ChoixVid][0]
            print(urlDL)
            DLFromYt(urlDL)
            if urls[ChoixVid][3] == "Compr1":
                nomVid = urls[ChoixVid][1].replace(".","") + ".mp4"
                print(nomVid)
                Vid = os.path.join('./videos',nomVid)
                VideoToFileNormal(Vid,urls[ChoixVid][1])
                
                os.remove(Vid)
                print(f"Deleted: {file_path}",end='\r')

            elif urls[ChoixVid][3] == "Compr2":
                nomVid = urls[ChoixVid][1].replace(".","") + ".mp4"
                Vid = os.path.join('./videos',nomVid)
                VideoToFileBig(Vid,urls[ChoixVid][1])
                os.remove(Vid)
                print(f"Deleted: {file_path}",end='\r')
            else:
                print("Description invalide")

        if ChoixCloud == 3:
            for i in range(len(urls)):
                print(i+1,urls[str(i+1)][1]+'\n')
            