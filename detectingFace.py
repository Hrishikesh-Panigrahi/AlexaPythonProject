from cv2 import cv2
import  cvzone
cap = cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # detecting face

overlay = cv2.imread('sunglass.png', cv2.IMREAD_UNCHANGED)

while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
    cv2.imshow('GG', frame)
    if cv2.waitKey(10) == ord('q'):
        break


