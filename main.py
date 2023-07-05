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

import os
import time



sys.path.append('tiktoka-studio-uploader-wanghaisheng-patch-4/examples')
from ytuploadnoapi import upload

if __name__ == '__main__':
    path = "grostest/"
    while True:
        time.sleep(10)
        files = os.listdir(path)
        if len(files) > 0:
            for file in files:
                actualfile = os.path.join(path, file)
                FileToImages(file)
                video_name = file + '.mp4'
                ImagesToVideo(video_name)
                upload(file,video_name,'Compr1',)
                os.remove(actualfile)
        delscreenrec = os.listdir('screen-recording/')
        if len(delscreenrec) > 0:
            for screenrec in delscreenrec:
                os.remove(os.path.join('screen-recording/', screenrec))