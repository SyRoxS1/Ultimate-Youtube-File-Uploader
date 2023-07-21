


This programs is used  to upload files to youtube, this is done by creating images containing the data of the the file then with all these images I can create a video then upload it to Youtube 

I did not have the original idea of it I saw it from https://github.com/DvorakDwarf/Infinite-Storage-Glitch/tree/master/src but thought it could be improved by having the script show the files on youtube showed as files in the script and i added the fact that you can automaticaly add the video generated to the channel using google api

This branch is in case you have to processe the file in a linux file systeme (from a apache website for example) and you dont have graphical interface so I transfert the video generated via a samba server to then be upload by youtube the main.py i meant to be ran on windows

You need to run linmain.py on the server without graphical interface and main.py on the one who has one, you have to configure main.py with the right parameter of the samba server.


Step by step guide to use the programme :

1: Get a webserver with a upload page or just use a simple folder on your computer where u can place things manually

2: Be sure to have python installed : https://www.python.org/downloads/ ( I use Python 3.10.2 if u have compatibility issue use this one : https://www.python.org/downloads/release/python-3102/ )

3 : Run the requierment file in the folder notes/ by using the command pip install -r requierments.txt ( if they are issues packages not found also do pip install -r requierments2.txt )

4 : Now you need to obtain you'r Cookie, you can do that by running the script GetCookie wich is present in the folder tiktoka-studio-uploader-.../examples/saveCookies.py (you need to have graphical interface to run it, it will open a browser and ask you to log in to google once you are logged in you need to close the BROWSER (don't stop the script it will do it itself after saving the cookie) the look for the YOUTUBEUPLOAD-cookie.json file wich should apear in the folder before example.

5 : Now that you have the cookie file place it wherever you want but note the path to it and place it the the file ytuploadnoapi.py in the CHANNEL_COOKIES variable, here you can also provide your youtube mail and password wich can solve some cookie issues and 

6 : Now you have to configure the linmain.py file, precise the path to your folder wich the files will automaticaly be converted into a video and also change the video_name variable, you can now start the script in the non graphical environement ( I recommend if you are on linux to use nohup python3 linmain.py command it will set the script to run in background as a process)

7 : Now time to change the main.py file you have to edit the variable local_videos_folder = '' wich is where the videos to upload will be stored after being pulled from the samba server (they will be deleted afterward), then the information of the samba server (if you dont use one for now you will have to edit manually but I will create a branche in the future) server_name = 'IF U USE DNS FOR SAMBA' server_ip = 'IP ADRESSE' server_share = 'THE NAME YOU GAVE YOUR SAMBA SHARE IN /etc/samba/smb.conf' username = 'USERNAME' password = 'PASSWORD'

The variable smbfolder is only usefull if you shared more than the folder in wich the videos are stored using samba, if you shared for example all the files you will put /home/user/files/ (the place where videos are), now if you only shared the folder containing video just put './' in the variable (nothing should also work)


Go check : https://github.com/wanghaisheng/tiktoka-studio-uploader

