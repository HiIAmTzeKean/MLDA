from flask import Flask, render_template, Response, request
import cv2
import datetime, time
import os, sys
import numpy as np
from threading import Thread

app = Flask(__name__, instance_relative_config=True,
            template_folder='templates')


# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

camera = cv2.VideoCapture(0)

@app.route('/')
def index():
    now=datetime.datetime.now() 
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('vid_{}.avi'.format(str(now).replace(":",'')), fourcc, 20.0, (640, 480))
    #Start new thread for recording the video
    thread = Thread(target = record, args=[out,])
    thread.start()

    #---- get ripeness value ----
    import subprocess
    import json
    import ast
    trying = subprocess.Popen("node flaskr/run-impluse.js flaskr/test.txt",\
                            shell=True, stdout=subprocess.PIPE)
    #--------- get location of the index -------
    result = trying.stdout.read().decode()
    rotten = result[result.index("value"):result.index("value")+15]
    result = result[result.index("value")+15:]
    ripe = result[result.index("value"):result.index("value")+15]
    #-------- -----
    return render_template('main.html', ripe=ripe, rotten=rotten)

@app.route('/ripe2')
def ripe2():
    import subprocess
    import json
    import ast
    trying = subprocess.Popen("node flaskr/run-impluse.js flaskr/test.txt",\
                            shell=True, stdout=subprocess.PIPE)
    #--------- get location of the index -------
    result = trying.stdout.read().decode()
    rotten = result[result.index("value"):result.index("value")+15]
    result = result[result.index("value")+15:]
    ripe = result[result.index("value"):result.index("value")+15]
    return render_template('scan.html', ripe=ripe, rotten=rotten)

@app.route('/ripe')
def ripe():
    now=datetime.datetime.now() 
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('vid_{}.avi'.format(str(now).replace(":",'')), fourcc, 20.0, (640, 480))
    #Start new thread for recording the video
    thread = Thread(target = record, args=[out,])
    thread.start()
    import random
    #--------- get location of the index -------
    rotten = random.randint(0,10)
    overipe = random.randint(0,10)
    ripe = 100 - overipe - rotten
    return render_template('main.html', ripe=ripe, rotten=rotten, overipe=overipe)

@app.route('/rotten')
def rotten():
    now=datetime.datetime.now() 
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('vid_{}.avi'.format(str(now).replace(":",'')), fourcc, 20.0, (640, 480))
    #Start new thread for recording the video
    thread = Thread(target = record, args=[out,])
    thread.start()
    import random
    #--------- get location of the index -------
    overipe = random.randint(0,10)
    ripe = random.randint(0,10)
    rotten = 100 - ripe - overipe
    return render_template('main.html', ripe=ripe, rotten=rotten, overipe=overipe)

@app.route('/overripe')
def overripe():
    now=datetime.datetime.now() 
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('vid_{}.avi'.format(str(now).replace(":",'')), fourcc, 20.0, (640, 480))
    #Start new thread for recording the video
    thread = Thread(target = record, args=[out,])
    thread.start()
    import random
    #--------- get location of the index -------
    rotten = random.randint(0,10)
    ripe = random.randint(0,10)
    overipe = 100 - ripe - rotten
    return render_template('main.html', ripe=ripe, rotten=rotten, overipe=overipe)

global rec, rec_frame, capture
rec =1
capture=0

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def record(out):
    global rec_frame
    while(rec):
        time.sleep(0.05)
        out.write(rec_frame)

def gen_frames():  # generate frame by frame from camera
    global out, capture,rec_frame
    while True:
        success, frame = camera.read() 
        if success: 
            if(capture):
                capture=0
                now = datetime.datetime.now()
                p = os.path.sep.join(['shots', "shot_{}.png".format(str(now).replace(":",''))])
                cv2.imwrite(p, frame)
            
            if(rec):
                rec_frame=frame
                frame= cv2.putText(cv2.flip(frame,1),"Recording...", (0,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),4)
                frame=cv2.flip(frame,1)
            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame,1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass
