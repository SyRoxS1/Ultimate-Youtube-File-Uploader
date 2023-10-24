import sys
from MainRisker import FileToImages
from FramesToVideoNormal import ImagesToVideo
from MainBigSafe import FileToImagesBig
from FramesToVideoSafe import ImagesBigToVideo
from VideoDownloader import DLFromYt
from VideoToFileNormal import VideoToFileNormal
from VideoToFileBig import VideoToFileBig
from GetYtVideosName import get_channel_videos
from VideoDownloader import DLFromYt
from RotateForShort import Rotate
from SplitVideo import split
import os
import time
from tkinter import Tcl
from ytuploadnoapi4 import instantpublish

if __name__ == '__main__':
    short = True
    path = "PUT FOLDER WHERE FILES HAVE TO BE UPLOADED TO YT ARE"
    while True:
        if short == True:
            files = os.listdir(path)
            if len(files) > 0:
                for file in files:
                    actualfile = os.path.join(path, file)
                    print(actualfile)
                    FileToImages(actualfile)
                    Rotate()
                    video_name = 'videos/' + file + '.mp4'
                    print(video_name)
                    ImagesToVideo(video_name)
                    split(video_name,file)
                    splitedvideos = os.listdir('videos/')
                    splitedvideos.remove('folder.txt')
                    splitedvideos = Tcl().call('lsort', '-dict', splitedvideos) #sort so the videos are uploaded in the right order

                    for vid in splitedvideos: #upload each part of the video
                        print(vid)
                        instantpublish(vid,'videos/'+vid,'Compr1')
                        os.remove('videos/'+vid)
                    os.remove(actualfile)
                    
            delscreenrec = os.listdir('screen-recording/')
            if len(delscreenrec) > 0:
                for screenrec in delscreenrec:
                    os.remove(os.path.join('screen-recording/', screenrec))
            time.sleep(5) 

        else:
            files = os.listdir(path)
            if len(files) > 0:
                for file in files:
                    actualfile = os.path.join(path, file)
                    print(actualfile)
                    FileToImages(actualfile)
                    video_name = 'videos/' + file + '.mp4'
                    print(video_name)
                    ImagesToVideo(video_name)
                    instantpublish(file,video_name,'Compr1',)
                    os.remove(actualfile)
                    os.remove(video_name)
            delscreenrec = os.listdir('screen-recording/')
            if len(delscreenrec) > 0:
                for screenrec in delscreenrec:
                    os.remove(os.path.join('screen-recording/', screenrec))
            time.sleep(5) 