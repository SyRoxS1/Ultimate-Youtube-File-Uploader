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



sys.path.append('tiktoka-studio-uploader/examples')
from ytuploadnoapi import upload

if __name__ == '__main__':
    short = True
    path = "TEST"
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
                    os.remove(video_name)
                    for vid in splitedvideos:
                        upload(vid,vid,'Compr1',)
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
                    
                    upload(file,video_name,'Compr1',)
                    os.remove(actualfile)
                    os.remove(video_name)
            delscreenrec = os.listdir('screen-recording/')
            if len(delscreenrec) > 0:
                for screenrec in delscreenrec:
                    os.remove(os.path.join('screen-recording/', screenrec))
            time.sleep(5) 