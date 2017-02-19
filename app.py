from flask import Flask, render_template
import datetime

app = Flask(__name__)

## Initializations 
global sessions
sessions = 0

## Settings
photos_per_session = 3
countdown_duration = 5

## Welcome-Screen
@app.route('/')
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
      'countdown': countdown_duration,
      'max_photos': photos_per_session
      }
    return render_template('photo_session.html', **templateData)

## Window to select which photos to print
@app.route('/printselection/', methods=['POST'])
def print_selection():
    return render_template('print.html', num_photos=photos_per_session)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


