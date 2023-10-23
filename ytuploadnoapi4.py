from tsup.youtube.youtube_upload import YoutubeUpload
from datetime import datetime, date, timedelta
import asyncio
from tsup.utils.webdriver.setupPL import checkRequirments
import os 

    # If it is the first time you've run the utility, a browser window should popup and prompt you to provide Youtube credentials. A token will be created and stored in request.token file in the local directory for subsequent use.

profilepath = (
    r"D:\Download\audio-visual\make-text-video\reddit-to-video\assets\profile\fastlane"
)
channel_cookie_path = r"D:\leo from old pc\programmation\python\FILE TO YT HOPEFULLY\BBBBBB\SYSYROCKS-cookie.json"

videopath = "file"
tags = "[desc]"
date_to_publish = ""
# if you use some kinda of proxy to access youtube,
proxy_option = ""

# for cookie issue,
video_title = "video_name"
video_title = video_title[:95]
username = ""
password = ""
video_description = "desc"
invalid_thumbnail = r""
thumbnail_local_path = r""


wait = 0
# 0-wait uploading done
# 1-wait Processing done
# 2-wait Checking done


# auto install requirments for user
# checkRequirments()
upload = YoutubeUpload(
    # use r"" for paths, this will not give formatting errors e.g. "\n"
    root_profile_directory="",
    proxy_option=proxy_option,
    is_open_browser=False,
    debug=True,
    use_stealth_js=False,
    # if you want to silent background running, set watcheveryuploadstep false
    channel_cookie_path=channel_cookie_path,
    username=username,
    browser_type="firefox",
    wait_policy="go next after copyright check success",
    password=password,
    is_record_video=True
    # for test purpose we need to check the video step by step ,
)
today = date.today()


def instantpublish(video_name,file,desc):
    asyncio.run(
        upload.upload(
            video_local_path=file,
            video_title=video_name,
            video_description=desc,
            thumbnail_local_path=thumbnail_local_path,
            tags=tags,
            publish_policy=1,
        )
    )

# friststart()
