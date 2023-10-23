from tsup.youtube.youtube_upload import YoutubeUpload
from datetime import datetime, date, timedelta
import asyncio
from tsup.utils.webdriver.setupPL import checkRequirments
import os

# If it is the first time you've run the utility, a browser window should popup and prompt you to provide Youtube credentials. A token will be created and stored in request.token file in the local directory for subsequent use.
def upload(video_name,file,desc):
    profilepath = (
        r"F:\programmation\FILE TO YT HOPEFULLY\BBBBBB\tiktoka-studio-uploader"
    )
    channel_cookie_path = r"D:\leo from old pc\programmation\python\FILE TO YT HOPEFULLY\BBBBBB\SYSYROCKS-cookie.json"

    videopath = file
    tags = [desc]
    date_to_publish = ""
    # if you use some kinda of proxy to access youtube,
    proxy_option = ""

    # for cookie issue,
    video_title = video_name
    video_title = video_title[:95]
    description = ""
    invalid_thumbnail = r""
    thumbnail_local_path = r""
    username = ""
    password = ""
    publish_policy=1
    wait = 1
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
        is_record_video=False,
        # for test purpose we need to check the video step by step ,
    )
    today = date.today()
    def checkfilebroken(path):
        print(f"check whether file exist{path}")
        if (os.path.exists(path)
            and os.path.getsize(path) > 0
        ):
            print(f'{path} is exist')
            return True
        else:
            print(f'{path} is not  exist')

            return False

    def instantpublish():
        asyncio.run(
            upload.upload(
                video_local_path=videopath,
                video_title=video_title,
                video_description=desc,
                thumbnail_local_path=thumbnail_local_path,
                tags=tags,
                publish_policy=1,
            )
        )


        # mode a:release_offset exist,publish_data exist will take date value as a starting date to schedule videos
        # mode b:release_offset not exist, publishdate exist , schedule to this specific date
        # mode c:release_offset not exist, publishdate not exist,daily count to increment schedule from tomorrow
        # mode d: offset exist, publish date not exist, daily count to increment with specific offset schedule from tomorrow

        #  if release_offset and not release_offset == "0-1":
        #             print('mode a sta',release_offset)
        #             if not int(release_offset.split('-')[0]) == 0:
        #                 offset = timedelta(months=int(release_offset.split(
        #                     '-')[0]), days=int(release_offset.split('-')[-1]))
        #             else:
        #                 offset = timedelta(days=1)
        #             if date_to_publish is None:
        #                 date_to_publish =datetime(
        #                     date.today().year,  date.today().month,  date.today().day, 10, 15)
        #             else:
        #                 date_to_publish += offset


    instantpublish()
    # friststart()
