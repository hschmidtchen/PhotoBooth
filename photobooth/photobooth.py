import os
import sqlite3
from flask import Flask, render_template, redirect
import datetime

app = Flask(__name__) #create app instance
app.config.from_object(__name__) #load config from this file

## Load default config and override config from an environment variable 
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'photobooth.db'),
    SECRET_KEY='devkey',
    USERNAME='admin',
    PASSWORD='default',
    photos_per_session = 3,
    countdown_duration = 5
))
app.config.from_envvar('PHOTOBOOTH_SETTINGS', silent=True)


## Initializations 
global sessions
sessions = 0

global image_path

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
    return render_template('instructions.html',session_id=sessions)

## Photo-Session (takes photos) --> updated for every photo
@app.route('/photo_session/<photo_id>', methods=['POST'])
def photo_session(photo_id):
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
    return render_template('printselection.html', num_photos=app.config['photos_per_session'])

## Window calling to wait during printing process
@app.route('/printing/<image_path>', methods=['GET', 'POST'])
def printing(image_path):
    ## printer communication goes here
    print(image_path)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


