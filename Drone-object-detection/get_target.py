import geopy
import geopy.distance
from math import tan ,atan,radians ,degrees,sqrt, pow
import numpy as np
import cv2
import cvzone
from calc_gps import gps
import time

cap = cv2.VideoCapture(0)

thres = 0.55
nmsThres = 0.2
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().split('\n')
print(classNames)
configPath = 'model_mobilenet.pbtxt'
weightsPath = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def object_detection_target(img):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cvzone.cornerRect(img, box)
            cv2.circle(img, (int(box[0]+box[2]/2),int(box[1]+box[3]/2)), 10, [0,0,255], 15)
            cv2.putText(img, "You are dead!! Goodbye :)",
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 0, 255), 2)
            cv2.imshow("Image", img)
            cv2.waitKey(1)

    except:
        cv2.imshow("Image", img)
        cv2.waitKey(1)

def object_detection(img):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
    try:
        for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cvzone.cornerRect(img, box)
            cv2.circle(img, (int(box[0]+box[2]/2),int(box[1]+box[3]/2)), 10, [0,255,0], 15)
            cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
                        (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        1, (0, 255, 0), 2)
            print("Object being detected is: ", classNames[classId - 1])
            cv2.imshow("Image", img)
            cv2.waitKey(1)
            time.sleep(1.5)
            return (box[0]+box[2]/2, box[1]+box[3]/2)
    except:
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        return (-1,-1)

def callback():
    while True:
        # define picture to_down' coefficient of ratio
        success, img = cap.read()
        scaling_factor = 0.5
        global count,bridge
        count = 0
        count = count + 1
        if count == 1:
            count = 0
            coord=object_detection(img)
            if (coord[0]!=-1):
                gps_coord=gps.compute_gps(gps, coord[0],coord[1],48.8,20.5,28.75119395,77.11790875,(5312,2800,0))
                print(gps_coord)
                return gps_coord
                #kamikaze(gps_coord)
        else:
            pass

if __name__ == '__main__':
    callback()