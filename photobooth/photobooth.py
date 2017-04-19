import os
import sqlite3
from flask import Flask, render_template, redirect, url_for
import subprocess
import datetime
from picamera import PiCamera
from time import sleep
from image import Image
import glob

app = Flask(__name__) #create app instance
app.config.from_object(__name__) #load config from this file

## Load default config and override config from an environment variable 
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'photobooth.db'),
    SECRET_KEY='devkey',
    USERNAME='admin',
    PASSWORD='default',
    photos_per_session = 1,
    countdown_duration = 5
))
app.config.from_envvar('PHOTOBOOTH_SETTINGS', silent=True)


## Initializations 
global sessions
use_dlr = True

## Database methods
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

## Welcome-Screen
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

## Instructions prior to each Photo-Session
@app.route('/instructions/')
def instructions():
    global sessions
    sessions=sessions+1
    #return render_template('instructions.html',session_id=sessions)
    return redirect(url_for('photo_session',photo_id=0))

## Photo-Session (takes photos) --> updated for every photo
@app.route('/photo_session/<photo_id>', methods=['GET','POST'])
def photo_session(photo_id):
    global use_dlr
    if use_dlr:
        Image.snap_dlr(sessions, photo_id)
    else:
        Image.snap(sessions,photo_id)
    templateData = {
      'session_id' : sessions,
      'photo_id': int(photo_id)+1,
      'countdown': app.config['countdown_duration'],
      'max_photos': app.config['photos_per_session']
      }
    return render_template('photo_session.html', **templateData)

## Window to select which photos to print
@app.route('/printselection/', methods=['POST'])
def print_selection():
    return render_template('printselection.html', num_photos=app.config['photos_per_session'],session_id=sessions)

## Window calling to wait during printing process
@app.route('/printing/', methods=['GET', 'POST'])
def printing():
    ## printer communication goes here
    global sessions
    #image_path = 'static/photos/print/print_'+str(sessions)+'.jpg'
    image_path = 'static/photos/print/image_'+str(sessions)+'_0.jpg'
    cmd=["./canon-selphy-print/print-selphy-card", str(image_path)]
    print(cmd)
    subprocess.call(cmd)
    sleep(15)
    return redirect('/')

def determine_session():
    max = -1
    for file in glob.glob('static/photos/full/image_*_0.jpg'):
        if int(file[25:-6])>max:
            max = int(file[25:-6])

    return max + 1

if __name__ == '__main__':
    sessions = determine_session()
    app.run(debug=True, host='0.0.0.0')


