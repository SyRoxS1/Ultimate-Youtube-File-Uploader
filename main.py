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

if __name__ == '__main__':
    channel_url = "https://www.youtube.com/channel/UCyj7svz9hL15ciYwrV_wpLg"
    path = "grostest/"
    while True:
        time.sleep(2)
        print("tour")
        files = os.listdir(path)
        if len(files) > 0:
            for file in files:
                actualfile = os.path.join(path, file)
                FileToImages(file)
                video_name = file + '.mp4'
                ImagesToVideo(video_name)
                upload(video_name,file,'Compr1','22','','public')
                os.remove(actualfile)