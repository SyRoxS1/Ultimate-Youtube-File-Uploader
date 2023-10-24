import cv2
import os
from tkinter import Tcl
from utils import binary_string_to_file

image_folder = 'videodebuild'
video_folder = './videos'
imageout_folder = 'videodebuild'

nomfichier = str('./videos/'+ input("Saisir le nom de la vidéo télécharger (sans l'extension): ")+'.mp4')
print(nomfichier)

final = str(input("Saisir le nom du fichier a recréer a partire de la vidéo (ne pas oublier l'extension .zip (ou autres)) : "))


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
    print(f"lecture de l'image : {image}",end="\r")
    for i in range(0,720,6):
        for j in range(0,1260,6):
            count += 1
            pixel= temp[i+3, j+2]
            moyenne += pixel[0]
            pixel= temp[i+3, j+3]
            moyenne += pixel[0]
            vraismoyenne = moyenne/2

            
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

binary_string_to_file(bin, final)

print("Vidéo convertie en fichier réussie !\n")

for filename in os.listdir(image_folder):
    if filename.endswith('.png'):
        file_path = os.path.join(image_folder, filename)
        os.remove(file_path)
        print(f"Deleted: {file_path}",end='\r')