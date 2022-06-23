import cv2

cv2.namedWindow("Camera")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
    # print(frame.shape)
    cv2.line(frame, (int(frame.shape[1]/2), 0), (int(frame.shape[1]/2), frame.shape[0]), (0, 0, 255), 2, 1)
else:
    rval = False

while rval:
    cv2.imshow("Camera", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(5)
    if key == 27: # exit on ESC
        break
    else:
        # Vertical Line
        cv2.line(frame, (int(frame.shape[1]/2), 0), (int(frame.shape[1]/2), frame.shape[0]), (0, 0, 255), 2, 1)
        # Horizontal Line
        cv2.line(frame, (int(frame.shape[0]/3), int(frame.shape[0]/2)), (int(frame.shape[0]), int(frame.shape[0]/2)), (0, 0, 255), 2, 1)

vc.release()
cv2.destroyWindow("Camera")