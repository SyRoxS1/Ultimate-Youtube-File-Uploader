Go check : https://github.com/wanghaisheng/tiktoka-studio-uploader 


This programs 'abuse' the fact that youtube doesn't have a limitation in uploading videos, so I use it to upload files this is done by creating images containing the data of the the file then with all these images I can create a video then upload it to Youtube 

I did not have the original idea of it I saw it from https://github.com/DvorakDwarf/Infinite-Storage-Glitch/tree/master/src but thought it could be improved by having the script show the files on youtube showed as files in the script and i added the fact that you can automaticaly add the video generated to the channel using google api

This branch is in case you have to processe the file in a linux file systeme (from a apache website for example) and you dont have graphical interface so I transfert the video generated via a samba server to then be upload by youtube the main.py i meant to be ran on windows

You need to run linmain.py on the server without graphical interface and main.py on the one who has one, you have to configure main.py with the right parameter of the samba server.


Step by step guide to use the programme :

1: Get a webserver with a upload page or just use a simple folder on your computer where u can place things manually

2: Be sure to have python installed : https://www.python.org/downloads/ ( I use Python 3.10.2 if u have compatibility issue use this one : https://www.python.org/downloads/release/python-3102/ )

3 : Run the requierment file in the folder notes/ by using the command pip install -r requierments.txt ( if they are issues packages not found also do pip install -r requierments2.txt )

4 : Now you need to obtain you'r 
