from PIL import Image
import time
import os
import numpy as np
from utils import file_to_binary_string

def putPixels(x, y, pixels):
    pixels[y:y+2, x:x+2] = np.array([0, 0, 0], dtype=np.uint8)

def resetPixels(width, height):
    return np.ones((height, width, 3), dtype=np.uint8)*255
 

 
fichiervoulue = input("Nom du fichier à convertir en vidéo (ne pas oublier l'extension) : ")





file_size_bytes = os.path.getsize(fichiervoulue)
size_bin_data = file_size_bytes * 8
print(size_bin_data)
 


 
img = Image.new('RGB', (1280, 720), 'white')
pixels = np.array(img, dtype=np.uint8)
 
x = 0
y = 0
count = 0
newcount = 0
nbimg = 1
cap = 230400
newcap = cap
finish = False
 

totalimg = size_bin_data // cap
fin = size_bin_data % cap
valeurimportant = totalimg *  230400 + fin
 




print("Nombre d'images à générer :", totalimg)
start_time = time.time()

with open(fichiervoulue, 'rb') as file:
    if count == 0:
        binary_string = file.read(28800)
        bin_data = ''.join(format(byte, '08b') for byte in binary_string)
    while not finish:
        while y < 779:
            while x < 1279:
                if nbimg == totalimg+1 and count == fin:
                    with open('endbalise.txt', 'r') as balise:
                        binbalise = balise.read()
                    while y < 779:
                        while x < 1279:
                            if finish:
                                x = 100000
                                y = 100000
                                break
                            if binbalise[newcount] == '0':
                                putPixels(x, y, pixels)
 
                            x += 2
                            if x == 1280:
                                x = 0
                                y += 2
                            newcount += 1
 
                            if newcount == 192:
                                img = Image.fromarray(pixels)
                                img.save(os.path.join('images', str(nbimg) + '.png'))
                                pixels = resetPixels(1280,720)
                                print("\033[2KLa fin.")
                                finish = True
                                break
                        
                if finish:
                    break
 
                if bin_data[count] == '0':
                    putPixels(x, y, pixels)
 
                count += 1
                x += 2
 
                if count == cap:
                    img = Image.fromarray(pixels)
                    img.save(os.path.join('images', str(nbimg) + '.png'))
                    print('Image number:', nbimg, 'on', totalimg + 1,end='\r')
                    pixels = resetPixels(1280,720)
                    nbimg += 1
                    x = 0
                    y = 0
                    count = 0
                    binary_string = file.read(28800)
                    bin_data = ''.join(format(byte, '08b') for byte in binary_string)
                    newcap += cap
 
            if finish:
                break
 
            y += 2
            x = 0
 
# Save the last image if it's not already saved
if not finish:
    img = Image.fromarray(pixels)
    img.save(os.path.join('images', str(nbimg) + '.png'))
 
end_time = time.time()
print("Images générées avec succès.")
print("Temps d'exécution :", end_time - start_time)