This branch is for automisation of the upload process so convert file into video and then upload the video

It necessite a graphical interface (i have only tested it on windows so i'm only sure for win os)

TUTORIAL : 


1: Get a webserver with a upload page or just use a simple folder on your computer where u can place things manually

2: Be sure to have python installed : https://www.python.org/downloads/ ( I use Python 3.10.2 if u have compatibility issue use this one : https://www.python.org/downloads/release/python-3102/ )

3 : Run the requierment file in the folder notes/ by using the command pip install -r requierments.txt ( if they are issues packages not found also do pip install -r requierments2.txt )

4 : Now you need to obtain you'r Cookies, you can do that by running the script GetCookie wich is present in the folder tiktoka-studio-uploader-.../examples/saveCookies.py, it will open a browser and ask you to log in to google once you are logged in you need to CLOSE THE BROWSER (don't stop the script it will do it itself after saving the cookie) the look for the YOUTUBEUPLOAD-cookie.json file wich should apear in the folder before example.

5 : Now that you have the cookie file place it wherever you want but note the path to it and place it the the file ytuploadnoapi.py in the CHANNEL_COOKIES variable, here you can also provide your youtube mail and password wich can solve some cookie issues and 

6 : Now time to change the main.py you just have to change the path variable and put the folder where file to convert are placed (note that once uploaded the file is deleted and the video wich is upload to youtube also)


Demonstration using Samba Server to retreive the files (cf code in ServerSide-Samba-To-Win branch)
<html>
  <body>
      https://youtu.be/pnchBKK11Fg
  </body>
</html>
