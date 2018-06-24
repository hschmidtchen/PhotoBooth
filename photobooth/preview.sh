#!/bin/sh
gphoto2 --capture-movie=7s --stdout> /home/pi/photobooth/photobooth/preview.mjpg & 
omxplayer /home/pi/photobooth/photobooth/preview.mjpg

gphoto2 --capture-image-and-download --filename $1