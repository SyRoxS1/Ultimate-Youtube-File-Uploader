from tsup.youtube.youtube_upload import YoutubeUpload
from datetime import datetime, date, timedelta
import asyncio
from tsup.utils.webdriver.setupPL import checkRequirments

def upload(video_name,file,desc):    
    # If it is the first time you've run the utility, a browser window should popup and prompt you to provide Youtube credentials. A token will be created and stored in request.token file in the local directory for subsequent use.

    profilepath = (
        r"F:\programmation\FILE TO YT HOPEFULLY\BBBBBB\tiktoka-studio-uploader-wanghaisheng-patch-4"
    )
    CHANNEL_COOKIES = r"D:\leo from old pc\programmation\python\FILE TO YT HOPEFULLY\BBBBBB\SYSYROCKS-cookie.json"
    publishpolicy=1
    videopath = file
    tags = [desc]
    date_to_publish = ""
    # if you use some kinda of proxy to access youtube,
    proxy_option = ""

    # for cookie issue,
    watcheveryuploadstep = False,
    title = video_name
    title = title[:95]
    username = ""
    password = ""
    description = desc
    invalid_thumbnail = r"../assets/hello.jpg"
    thumbnail = r"../assets/hello.jpg"
    publishpolicy = 1

    closewhen100percent = 0
    # 0-wait uploading done
    # 1-wait Processing done
    # 2-wait Checking done


    # auto install requirments for user
    # checkRequirments()
    upload = YoutubeUpload(
        # use r"" for paths, this will not give formatting errors e.g. "\n"
        root_profile_directory="",
        proxy_option=False,
        headless=False,
        debug=True,
        # if you want to silent background running, set watcheveryuploadstep false
        
        CHANNEL_COOKIES=CHANNEL_COOKIES,
        username=username,
        browserType="firefox",
        closewhen100percent="go next after copyright check success",
        password=password,
        recordvideo=False
        # for test purpose we need to check the video step by step ,
    )
    today = date.today()


    def instantpublish():
        asyncio.run(
            upload.upload(
                videopath=videopath,
                title=title,
                description=description,
                thumbnail=thumbnail,
                tags=tags,
                publishpolicy=1,
            )
        )





    instantpublish()
    # friststart()
