import cv2
import os
from tkinter import Tcl

def ImagesToVideo(video_name):    
    image_folder = 'images'
    
    
    
    
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
    
    for filename in os.listdir(image_folder):
        if filename.endswith('.png'):
            file_path = os.path.join(image_folder, filename)
            os.remove(file_path)
            print(f"Deleted: {file_path}",end='\r')