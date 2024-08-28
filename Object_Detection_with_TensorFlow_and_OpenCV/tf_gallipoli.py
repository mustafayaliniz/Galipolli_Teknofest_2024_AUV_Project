import numpy as np
import os
import tensorflow as tf
import cv2
from object_detection.utils import label_map_util

"""
@author: MUSTAFA YALINIZ
"""



PATH_TO_CKPT = os.path.join('frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join('mscoco_label_map.pbtxt')
NUM_CLASSES = 90


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

# Etiket haritasının yüklenmesi
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Video akışının başlatılması
cap = cv2.VideoCapture(0)

# Video ekran boyutunu ayarla
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

start_time=cv2.getTickCount()
# FPS değerini al
fps = cap.get(cv2.CAP_PROP_FPS)

with detection_graph.as_default():
    with tf.compat.v1.Session(graph=detection_graph) as sess:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            end_time=cv2.getTickCount()
            elapsed_time=(end_time-start_time)/cv2.getTickFrequency()
            fps=1/elapsed_time

            image_np_expanded = np.expand_dims(frame, axis=0)

            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})

            for i in range(len(boxes[0])):
                if scores is None or scores[0][i] > 0.5:
                    ymin, xmin, ymax, xmax = tuple(boxes[0][i].tolist())
                    (left, right, top, bottom) = (xmin * frame.shape[1], xmax * frame.shape[1],
                                                  ymin * frame.shape[0], ymax * frame.shape[0])
                    left, right, top, bottom = int(left), int(right), int(top), int(bottom)
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, str(categories[int(classes[0][i])]['name']), (left, top),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            cv2.putText(frame, f"FPS: {fps}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 1)
            start_time=end_time
            cv2.imshow('Object Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
