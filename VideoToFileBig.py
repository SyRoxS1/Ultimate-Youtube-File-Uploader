import cv2
import os
from tkinter import Tcl


image_folder = 'videodebuild'
video_folder = './videos'
imageout_folder = 'videodebuild'

nomfichier = str('./downloaded/'+ input("Saisir le nom de la vidéo télécharger : ")+'.mp4')
print(nomfichier)

final = str(input("Saisir le nom du fichier a recréer a partire de la vidéo (ne pas oublier l'extension .zip) : "))


#images big 720*1260



vidcap = cv2.VideoCapture(nomfichier)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./videodebuild/frame%d.png" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1


images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

images = Tcl().call('lsort', '-dict', images)

bin = []
count=0
moyenne = 0
for image in images:
    temp= cv2.imread("./"+image_folder+"/"+image)
    for i in range(0,720,6):
        for j in range(0,1260,6):
            count += 1
            pixel= temp[i, j]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i, j+1]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i, j+2]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i, j+3]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i, j+4]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i, j+5]
            for couleur in pixel:
                moyenne = moyenne + couleur



            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+1, j+1]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+1, j+2]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+1, j+3]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+1, j+4]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+1, j+5]
            for couleur in pixel:
                moyenne = moyenne + couleur


            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+2, j+1]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+2, j+2]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+2, j+3]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+2, j+4]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+2, j+5]
            for couleur in pixel:
                moyenne = moyenne + couleur



            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+3, j+1]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+3, j+2]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+3, j+3]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+3, j+4]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+3, j+5]
            for couleur in pixel:
                moyenne = moyenne + couleur


            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+4, j+1]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+4, j+2]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+4, j+3]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+4, j+4]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+4, j+5]
            for couleur in pixel:
                moyenne = moyenne + couleur


            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+5, j+1]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+5, j+2]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+5, j+3]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+5, j+4]
            for couleur in pixel:
                moyenne = moyenne + couleur
            pixel= temp[i+5, j+5]
            for couleur in pixel:
                moyenne = moyenne + couleur
            
            vraismoyenne = moyenne/108

            
            if vraismoyenne < 155 and vraismoyenne > 100:
                print("nahhhhhhh")
                print(vraismoyenne)
            if vraismoyenne < 127:
                bin.append(0)
            else:
                bin.append(1)
            moyenne = 0

print("Conversion des bits en fichier...\n")
bin = ''.join(map(str,bin))
b = bin.find('011101110111011101110111001011100111100101101111011101010111010001110101011000100110010100101110011000110110111101101101001011110110110101110010011001100111001001101001011100000110111101101110')
bin = bin[:b]

#bin = "0b" + bin

bytesvar = int(bin, 2).to_bytes((len(bin) + 7) // 8, byteorder='big')
bytesvar = bytes('P', 'utf-8') + bytesvar[2:]

with open(final, 'wb') as f:
    f.write(bytesvar)
print("Vidéo convertie en fichier réussie !\n")