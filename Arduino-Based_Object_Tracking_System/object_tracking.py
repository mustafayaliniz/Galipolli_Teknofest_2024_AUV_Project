import cv2
import imutils
import time
import serial

"""
@author: MUSTAFA YALINIZ
"""


arduino = serial.Serial(port='COM10', baudrate=9600, timeout=1)


blue_low = (100, 100, 50)  
blue_high = (140, 255, 255)  
a = 0
b = 0
xc = 0
yc = 0
vs = cv2.VideoCapture(0)
time.sleep(0.1)

while True:
    ret, frame = vs.read()

    if not ret:
        break

    frame = imutils.resize(frame, width=1080)
    h, w = frame.shape[:2]
    cx = int(w / 2)
    cy = int(h / 2)
    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blue_low, blue_high)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        xc = int(M["m10"] / M["m00"])
        yc = int(M["m01"] / M["m00"])
        center = (xc, yc)

        if radius > 10:
            cv2.rectangle(frame, (int(x - radius), int(y - radius)), (int(x + radius), int(y + radius)), (255, 0, 255),
                          3)

    cv2.circle(frame, center, 5, (0, 0, 0), -1)
    a = xc - cx
    b = cy - yc
    arduino.write(f"{a},{b}\n".encode())
    data = arduino.readline().decode().strip()
    print(data) # printing the value
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vs.release()
cv2.destroyAllWindows()
