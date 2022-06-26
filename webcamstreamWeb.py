import sys
sys.path.append('/usr/include/opencv')

import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)

# manager = Manager(app)

vc = cv2.VideoCapture(-1)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        rval, frame = vc.read()
        if frame != None:
            # Vertical Line
            cv2.line(frame, (int(frame.shape[1]/2), 0), (int(frame.shape[1]/2), frame.shape[0]), (0, 0, 255), 2, 1)
            # Horizontal Line
            cv2.line(frame, (int(frame.shape[0]/3), int(frame.shape[0]/2)), (int(frame.shape[0]), int(frame.shape[0]/2)), (0, 0, 255), 2, 1)

        if not rval:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, threaded = True)
    # manager.run()