This programs is used  to upload files to youtube, this is done by creating images containing the data of the the file then with all these images I can create a video then upload it to Youtube 

I did not have the original idea of it I saw it from [DvorakDwarf "Infinite-Storage-Glitch"](https://github.com/DvorakDwarf/Infinite-Storage-Glitch/tree/master/src) but thought it could be improved by having the script show the files on youtube showed as files in the script and i added the fact that you can automaticaly add the video generated to the channel using youtube api ( 6 videos per days :'( , go check other branch for bypass using [tiktoka-studio-uploader](https://github.com/wanghaisheng/tiktoka-studio-uploader) )

So the main branch of this programme is really almost the same as DvorakDwarf the only thing I have added is the YoutubeAsCloud feature that allow the user to input a channel url and it list all the videos (using api) and then ask the user wich one he wants to download its not the best yet but it might be upgraded, if you just want to use it to conver video to file or file to video chose option 1 or 2 they should work fine

I recomend you check the [WindowsServerSide](https://github.com/SyRoxS1/Ultimate-Youtube-File-Uploader/tree/main/Srv-Win) branch (wich is now merged to main) if you need some automatisation of the programme it allow the user to have a folder in wich every files that is placed is converted into video and then upload to youtube with the data needed to reverse the operation, You can also check the not yet finished GUI branch wich still use the api to gather the information about the channel and displays the file.


Installation :

[IMPORTANT NOTE] : This code is tested on python 3.10.16, version from python 3.12 break packages installation

Clone the repository :

1 : git clone https://github.com/SyRoxS1/Ultimate-Youtube-File-Uploader.git

Go into the directory :

2 : cd Ultimate-Youtube-File-Uploader

Create a virtual environement

3 : python -m venv .env

Activate it :

4 : source .env/bin/activate

Install dependencies :

5 : pip install -r notes/requirements.txt

Running the programme :

6 : python main.py
