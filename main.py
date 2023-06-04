if __name__ == '__main__':
    PremierChoix = int(input("Vidéo -> Fichier (1)\nFichier -> Vidéo (2)\nYoutubeAsAcloud (beta)(3): "))
    if PremierChoix == 1:
        import VideoDownloader
        TypeVideo = int(input("Saisire le type de vidéo : (1) : Normale (2) : Insecure : "))
        if TypeVideo == 1:
            import VideoToFileNormal
        if TypeVideo == 2:
            import VideoToFileBig
        
    if PremierChoix == 2:
        ChoixCompr = int(input(f"Niveau de sureté voulu ? : \n 1 : Faible (plus de risque de corruption mais plus rapide)\n2 : Fort (l'inverse)\n"))
    
        if ChoixCompr == 1:
            import MainRisker
            import FramesToVideoNormal
            import UploadeToYt
        if ChoixCompr == 2:
            import MainBigSafe
            import FramesToVideoSafe

    if PremierChoix == 3:
        import GetYtVideosName
        ChoixCloud = int(input("Ajouter des fichiers (1), Extraire des fichiers(2) : "))
        if ChoixCloud == 1:
            print(1)
        if ChoixCloud == 2:
            print(2)
