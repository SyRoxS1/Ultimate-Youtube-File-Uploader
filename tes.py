import os
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
from ytuploadnoapi3 import upload


splitedvideos = os.listdir('videos/')
splitedvideos = splitedvideos[1:]


for vid in splitedvideos:
    print(vid)
    upload(vid,'videos/'+vid,'Compr1')
    os.remove('videos/'+vid)
