
from MainRisker import FileToImages
from FramesToVideoNormal import ImagesToVideo
from MainBigSafe import FileToImagesBig
from FramesToVideoSafe import ImagesBigToVideo
from VideoDownloader import DLFromYt
from VideoToFileNormal import VideoToFileNormal
from VideoToFileBig import VideoToFileBig
from GetYtVideosName import get_channel_videos
from UploadeToYt import upload
from VideoDownloader import DLFromYt
import os
import time

#This script is meant to be run on the machine without graphical interface

if __name__ == '__main__':
    channel_url = "https://www.youtube.com/channel/UCyj7svz9hL15ciYwrV_wpLg"
    path = "/home/user/files/"
    while True:
        time.sleep(10)
        files = os.listdir(path)
        if len(files) > 0:
            for file in files:
                actualfile = os.path.join(path, file)
                print(actualfile)
                FileToImages(actualfile)
                video_name = '/root/BBBBBB/videos/' + file + '.mp4'
                print(video_name)
                ImagesToVideo(video_name)
                os.remove(actualfile)


