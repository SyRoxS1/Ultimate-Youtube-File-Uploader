import codecs
from PIL import Image
import numpy as np
import os


def putPixels(x, y, pixels):
    pixels[y:y+6, x:x+6] = np.array([0, 0, 0], dtype=np.uint8)

def resetPixels(width, height):
    return np.ones((height, width, 3), dtype=np.uint8)*255

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

fichiervoulue = str(input("Nom du fichier a convertire en vidéo (sans oublier l'extension) : \n"))


file_size_bytes = os.path.getsize(fichiervoulue)
size_bin_data = file_size_bytes * 8

img = Image.new('RGB', (1260, 720), 'white')
pixels = np.array(img, dtype=np.uint8)

x = 0
y = 0
count = 0
nbimg = 1
cap = 25200
newcap = cap
finish = False

totalimg = size_bin_data // cap
fin = size_bin_data % cap
valeurimportant = totalimg *  cap + fin
newcount = 0

print("Nombre d'images a générer :",totalimg+1)
with open(fichiervoulue, 'rb') as file:
    if count == 0:
        binary_string = file.read(3150)
        bin_data = ''.join(format(byte, '08b') for byte in binary_string)
    
    while finish != True:
        while y < 715:
            while x < 1255:
                if nbimg == totalimg+1 and count == fin:
                    with open('endbalise.txt','r') as balise:
                        binbalise = balise.read()
                    while y < 715:
                        while x < 1255:
                            if finish:
                                x = 100000
                                y = 100000
                                break

                            if binbalise[newcount] == '0':
                                putPixels(x, y, pixels)
                            x += 6
                            if x == 1260:
                                x = 0
                                y += 6
                            newcount += 1
                            if newcount == 192:
                                img = Image.fromarray(pixels)
                                img.save(os.path.join('imagesbig', str(nbimg) + '.png'))
                                pixels = resetPixels(1260,720)
                                print("la fin.")
                                finish = True
                                x = 50000
                                y = 50000
                                break
                
                if finish == True:
                    break

                if bin_data[count] == '0':
                    putPixels(x, y, pixels)
                    
                count += 1
                x = x + 6

                if count == cap:
                    img = Image.fromarray(pixels)
                    img.save(os.path.join('imagesbig', str(nbimg) + '.png'))
                    print('Image number:', nbimg, 'on', totalimg + 1,end='\r')
                    pixels = resetPixels(1260,720)
                    nbimg += 1
                    x = 0
                    y = 0
                    count = 0
                    binary_string = file.read(3150)
                    bin_data = ''.join(format(byte, '08b') for byte in binary_string)
                    newcap += cap
                
            if finish:
                break

            y = y + 6
            x = 0
    
            

print("gg")

