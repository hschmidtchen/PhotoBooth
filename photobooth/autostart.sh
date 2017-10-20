#!/bin/sh
cd photobooth/photobooth

#disable mouse pointer
unclutter -idle 0.05 -root &

#clear CUPS queue
cancel -a -

#start flask app
python photobooth.py &

#open browser
chromium-browser --noerrdialogs --kiosk --incognito 127.0.0.1:5000