from MainRisker import FileToImages
from FramesToVideoNormal import ImagesToVideo
from MainBigSafe import FileToImagesBig
from FramesToVideoSafe import ImagesBigToVideo
from VideoDownloader import DLFromYt
from VideoToFileNormal import VideoToFileNormal
from VideoToFileBig import VideoToFileBig
from GetYtVideosName import get_channel_videos
from UploadeToYt import upload

if __name__ == '__main__':
    PremierChoix = int(input("Vidéo -> Fichier (1)\nFichier -> Vidéo (2)\nYoutubeAsAcloud (beta)(3): "))
    if PremierChoix == 1:
        url = str(input('Saisir url a convertire en fichier : ' ))
        DLFromYt(url)

        TypeVideo = int(input("Saisire le type de vidéo : (1) : Normale (2) : Insecure : "))
        if TypeVideo == 1:
            nomfichier = str('./downloaded/'+ input("Saisir le nom de la vidéo télécharger (sans l'extension) : ")+'.mp4')
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
            fichiervoulue = str(input("Nom du fichier à convertir en vidéo (ne pas oublier l'extension) : "))
            FileToImages(fichiervoulue)
            
            video_name = fichiervoulue + '.mp4'
            ImagesToVideo(video_name)

            #import UploadeToYt
        if ChoixCompr == 2:
            fichiervoulue = str(input("Nom du fichier a convertire en vidéo (sans oublier l'extension) : \n"))
            FileToImagesBig(fichiervoulue)

            video_name = fichiervoulue + '.mp4'
            ImagesBigToVideo(video_name)

    if PremierChoix == 3:
        channel_url = input('Enter a YouTube channel URL: ')
        
        urls = get_channel_videos(channel_url)
        print(urls)
        ChoixCloud = int(input("Ajouter des fichiers (1), Extraire des fichiers(2) : "))
        if ChoixCloud == 1:
            ChoixCompr = int(input(f"Niveau de sureté voulu ? : \n 1 : Faible (plus de risque de corruption mais plus rapide)\n2 : Fort (Meme vitesse mais plus gros fichier vidéo)\n"))
    
            if ChoixCompr == 1:
                fichiervoulue = str(input("Nom du fichier à convertir en vidéo (ne pas oublier l'extension) : "))
                FileToImages(fichiervoulue)
                
                video_name = fichiervoulue + '.mp4'
                ImagesToVideo(video_name)
                upload(video_name,video_name,'Compr1','22','','private')
                
            if ChoixCompr == 2:
                fichiervoulue = str(input("Nom du fichier a convertire en vidéo (sans oublier l'extension) : \n"))
                FileToImagesBig(fichiervoulue)
    
                video_name = fichiervoulue + '.mp4'
                ImagesBigToVideo(video_name)
                upload(video_name,video_name,'Compr2','22','','private')
                
        if ChoixCloud == 2:
            print(2)
