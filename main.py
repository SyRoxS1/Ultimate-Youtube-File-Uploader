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

#This script is meant to be run on the machine with a graphical interface

sys.path.append('tiktoka-studio-uploader-wanghaisheng-patch-4/examples')
from ytuploadnoapi import upload
from smb.SMBConnection import SMBConnection
if __name__ == '__main__':
    
    local_videos_folder = 'videos/'
    server_name = ''
    server_ip = ''
    server_share = ''
    username = ''
    password = ''
    while True:
        
        conn = SMBConnection(username, password, '', server_name)
        conn.connect(server_ip)

        # List files in the shared folder
        files = conn.listPath(server_share, '/root/BBBBBB/videos/')
        if len(files) > 1:
            for file in files:
                print(file.filename)
                if file.filename.endswith('.mp4'):
                    local_file_path = os.path.join(local_videos_folder, file.filename)
                    with open(local_file_path, 'wb') as f:
                        conn.retrieveFile(server_share, '/root/BBBBBB/videos/'+file.filename, f)
                    conn.deleteFiles(server_share, '/root/BBBBBB/videos/'+ file.filename)
        conn.close()
        
        path = 'videos/'
        files = os.listdir(path)
        if len(files) > 1:
            for file in files:
                if file.endswith('.mp4'):
                    video_name = os.path.join(path, file)
                    upload(file,video_name,'Compr1',)
                    os.remove(video_name)
        delscreenrec = os.listdir('screen-recording/')
        if len(delscreenrec) > 0:
            for screenrec in delscreenrec:
                os.remove(os.path.join('screen-recording/', screenrec))
        time.sleep(10)
