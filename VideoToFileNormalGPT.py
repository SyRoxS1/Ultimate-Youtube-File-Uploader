import cv2
import os
from tkinter import Tcl
import numpy as np
import time

image_folder = 'videodebuild'
video_folder = './videos'
imageout_folder = 'videodebuild'

nomfichier = str('./downloaded/'+ input("Saisir le nom de la vidéo télécharger : ")+'.mp4')
print(nomfichier)

final = str(input("Saisir le nom du fichier a recréer a partire de la vidéo (ne pas oublier l'extension .zip) : "))

vidcap = cv2.VideoCapture(nomfichier)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("./videodebuild/frame%d.png" % count, image)  
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
start_time = time.time()
images = Tcl().call('lsort', '-dict', images)
error = 0
bin = []
count=0
moyenne = 0
for image in images:
    print("lecture de l'image",count,"sur",len(images))
    end_time = time.time()
    print("Temps d'exécution :", end_time - start_time)
    start_time = time.time()
    count += 1
    temp = image.load()
    for i in range(0,720,2):
        for j in range(0,1280,2):
            pixel= temp[i, j]
            for couleur in pixel:
                moyenne += couleur
            pixel= temp[i, j+1]
            for couleur in pixel:
                moyenne += couleur
            pixel= temp[i+1, j]
            for couleur in pixel:
                moyenne += couleur
            pixel= temp[i+1, j+1]
            for couleur in pixel:
                moyenne += couleur
            
            vraismoyenne = moyenne/12
            
            if vraismoyenne < 155 and vraismoyenne > 100:
                error += 1
               
            if vraismoyenne < 127:
                bin.append(0)
            else:
                bin.append(1)
            moyenne = 0
            

                
            
bin = ''.join(map(str,bin))
b = bin.find('011101110111011101110111001011100111100101101111011101010111010001110101011000100110010100101110011000110110111101101101001011110110110101110010011001100111001001101001011100000110111101101110')
bin = bin[:b]

#bin = "0b" + bin

bytesvar = int(bin, 2).to_bytes((len(bin) + 7) // 8, byteorder='big')
bytesvar = bytes('P', 'utf-8') + bytesvar[2:]

with open(final, 'wb') as f:
    f.write(bytesvar)

print("close : ",error)
print("Vidéo convertie en fichier réussie !\n")