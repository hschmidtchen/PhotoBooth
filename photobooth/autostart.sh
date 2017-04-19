#!/bin/sh
cd photobooth/photobooth

python photobooth.py &

chromium-browser --kiosk 127.0.0.1:5000