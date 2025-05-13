import cv2
import os
from tkinter import Tcl
import numpy as np
from utils import binary_string_to_file, append_binary_chunk_to_file
import time
    
    
def VideoToFileNormal(nomfichier,final):
    imageout_folder = 'videodebuild'
    image_folder = 'videodebuild'
    video_folder = './videos'
    
    
    
    
    vidcap = cv2.VideoCapture(nomfichier)
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite("./videodebuild/frame%d.png" % count, image)  
      success,image = vidcap.read()
      print(f'Read {count} frames...', end='\r')
      count += 1
    nb_images = count
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    
    images = Tcl().call('lsort', '-dict', images)
    error = 0
    bin = []
    count=0
    moyenne = 0
    
    #TEMP
    nb_images = 700

    for image in images:
        print("lecture de l'image",count+1,"sur",len(images),end="\r")
        count += 1
        temp= cv2.imread("./"+image_folder+"/"+image)
        
        for i in range(0,720,2):
            for j in range(0,1280,2):
                pixel= temp[i, j]
                moyenne += pixel[0]
                pixel= temp[i, j+1]
                moyenne += pixel[0]
                pixel= temp[i+1, j]
                moyenne += pixel[0]
                pixel= temp[i+1, j+1]
                moyenne += pixel[0]
                
                vraismoyenne = moyenne/4
                
                if vraismoyenne < 155 and vraismoyenne > 100:
                    error += 1
                
                if vraismoyenne < 127:
                    bin.append(0)
                else:
                    bin.append(1)
                moyenne = 0
            
        if nb_images > 600:
            if bin != []:
                if count == nb_images:
                    bin = ''.join(map(str,bin))
                    b = bin.find('011101110111011101110111001011100111100101101111011101010111010001110101011000100110010100101110011000110110111101101101001011110110110101110010011001100111001001101001011100000110111101101110')
                    bin = bin[:b]
                    append_binary_chunk_to_file(bin, final)
                else:
                    append_binary_chunk_to_file(bin, final)
            bin = []

        
    bin = ''.join(map(str,bin))
    b = bin.find('011101110111011101110111001011100111100101101111011101010111010001110101011000100110010100101110011000110110111101101101001011110110110101110010011001100111001001101001011100000110111101101110')
    bin = bin[:b]
    
    
    if nb_images < 600:
        binary_string_to_file(bin, final)
    
    
    print("\nClose pixels (shouldn't be an issue) : ",error)
    
    print("Vidéo convertie en fichier réussie !\n")
    for filename in os.listdir(image_folder):
        if filename.endswith('.png'):
            file_path = os.path.join(image_folder, filename)
            os.remove(file_path)
            print(f"Deleted: {file_path}",end='\r')


