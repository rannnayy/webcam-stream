# Webcam Stream

## How to Run
1. Webcam Stream (streaming directly using window)
- Run ```webcamstream.py```
- To exit from window, press ```esc``` button on your keyboard
<br>

2. Webcam Stream on Web
- Run ```webcamstreamWeb.py```
- Open browser using ```ctrl+click``` on prompted message from terminal. It is usually ip:5000.
 Upon remote access using other device. It should be performed on devices connected on same network.
 Open 0.0.0.0:5000 or 192.168.0.8:5000, or you can also see the link prompted on terminal upon running server.

pip2 install opencv-python==4.2.0.32

# Using uWSGI Command Line
uwsgi uwsgi.ini --socket 0.0.0.0:8000 --protocol=http --lazy -w wsgi:app

# Using uWSGI Script
uwsgi --ini uwsgi.ini