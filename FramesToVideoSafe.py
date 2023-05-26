import cv2
import os
from tkinter import Tcl


image_folder = 'imagesbig'


video_name = str(input('Saisir le nom de la vidéo a enrengistrer : ') + '.mp4')

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
video = cv2.VideoWriter(video_name, fourcc, 30, (width,height))
images = Tcl().call('lsort', '-dict', images)
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()