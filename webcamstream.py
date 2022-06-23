import cv2

cv2.namedWindow("Camera")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
    # print(frame.shape)
    cv2.line(frame, (int(frame.shape[1]/2), 0),(int(frame.shape[1]/2), frame.shape[0]), (255, 0, 0), 10, 1)
else:
    rval = False

while rval:
    cv2.imshow("Camera", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(5)
    if key == 27: # exit on ESC
        break
    else:
        cv2.line(frame, (int(frame.shape[1]/2), 0),(int(frame.shape[1]/2), frame.shape[0]), (255, 0, 0), 10, 1)
        cv2.line(frame, (0, int(frame.shape[0]/2)),(frame.shape[1], int(frame.shape[0]/2)), (255, 0, 0), 10, 1)

vc.release()
cv2.destroyWindow("Camera")