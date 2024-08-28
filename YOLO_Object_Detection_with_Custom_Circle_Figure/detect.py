import cv2
from ultralytics import YOLO
import time

model = YOLO("best.pt")

prev_frame_time = 0
new_frame_time = 0

cap = cv2.VideoCapture(0)

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    ret, img = cap.read()



    img = cv2.resize(img, (1280, 720))


    results = model(img)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0][:4])
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print("fps: ", fps)

    cv2.imshow('img', img)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
