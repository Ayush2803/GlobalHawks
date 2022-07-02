from __future__ import print_function
import time
import math
import threading
import cv2
#from dronekit import connect, VehicleMode, LocationGlobalRelative
#from pymavlink import mavutil

from get_target import *
'''
# Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None


# Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()


# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect("127.0.0.1:14550", wait_ready=True)

def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration, drone):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = drone.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)


    # send command to vehicle on 1 Hz cycle
    for x in range(0,duration):
        drone.send_mavlink(msg)
        time.sleep(1)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    
    
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
                             
    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude
    
    # Wait until the vehicle reaches a safe height before processing the goto
    #  (otherwise the command after Vehicle.simple_takeoff will execute
    #   immediately).
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)
       
    
arm_and_takeoff(15)


print("Set default/target airspeed to 3")
vehicle.airspeed = 6
#current coordinates:
vehicle.currentlocation = vehicle.location.global_frame
x0 = vehicle.location.global_frame.lat
y0 = vehicle.location.global_frame.lon
'''
x0 = -35.36330460
y0 = 149.16520547
#target coordinates:
#x = -35.36423292
#y = 149.16467194
#x = -35.36251608
#y = 149.16512491
x,y = callback()

x1 = 2*x - x0
y1 = 2*y - y0
print("This is the point in ground ()")
print(x1, y1)
print("Drone going towards target")

# classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nmsThres)
#     try:
#         for classId, conf, box in zip(classIds.flatten(), confs.flatten(), bbox):
#             cvzone.cornerRect(img, box)
#             cv2.circle(img, (int(box[0]+box[2]/2),int(box[1]+box[3]/2)), 10, [0,255,0], 15)
#             cv2.putText(img, f'{classNames[classId - 1].upper()} {round(conf * 100, 2)}',
#                         (box[0] + 10, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL,
#                         1, (0, 255, 0), 2)
#             #print("Object being detected is: ", classNames[classId - 1])
#             cv2.imshow("Image", img)
#             cv2.waitKey(1)

#             return (box[0]+box[2]/2, box[1]+box[3]/2)
#     except:
#         cv2.imshow("Image", img)
#         cv2.waitKey(1)
#         return (-1,-1)

cap = cv2.VideoCapture(0)
while True:
    success , img= cap.read()
    junk=object_detection_target(img)
    
#time.sleep(1000)
'''
point1 = LocationGlobalRelative(x1, y1, -100)
vehicle.simple_goto(point1, groundspeed=14)
print("Going to Target!")
vehicle.simple_goto(point1, groundspeed=14)
while True:
	print(" Altitude: ", vehicle.location.global_relative_frame.alt)
	print(" Velocity: ", vehicle.velocity)
	print(" GSpeed: ", vehicle.groundspeed)
time.sleep(20)

# Shut down simulator if it was started.
if sitl:
    sitl.stop()
'''