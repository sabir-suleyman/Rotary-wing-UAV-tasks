#!/usr/bin/env python3
#
#       Sabir Süleymanlı <suleymanlisabir3@gmail.com>
#       
#       main.py            07.07.2022           
#       

from os import close

from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
from threading import Thread
import time  # mavlink mavproxy
import math

str_mode = ""
def Servo(pvm, slp):
    msg = vehicle.message_factory.command_long_encode(
        0, 0,  # target system, target component
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,  # komut
        0,  # confirmation
        9,  
        pvm,  #
        0, 0, 0, 0, 0)  

    vehicle.send_mavlink(msg)
    time.sleep(slp)
    return

def arm_and_takeoff(tgt_altitude):
    global vehicle

    while not vehicle.is_armable:
        print("waiting to be armable")
        time.sleep(1)
    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed: time.sleep(1)
    print("Takeoff")
    time.sleep(2)
    vehicle.simple_takeoff(tgt_altitude)
    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(">> Altitude = %.1f m" % altitude)
        if altitude >= tgt_altitude - 1:
            print("Altitude reached")
            break
        time.sleep(1)

def clear_mission():
    global vehicle

    cmds = vehicle.commands
    vehicle.commands.clear()
    vehicle.flush()

    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()


def download_mission():
    global vehicle

    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()

def get_current_mission():
    global vehicle

    print("Downloading mission")
    download_mission()
    missionList = []
    n_WP = 0

    for wp in vehicle.commands:
        missionList.append
    missionList = []
    n_WP = 0

    for wp in vehicle.commands:
        missionList.append(wp)
        n_WP += 1(wp)
        n_WP += 1

    return n_WP, missionList

def add_last_waypoint_to_mission(wp_Last_Latitude, wp_Last_Longitude, wp_Last_Altitude):
    global vehicle

    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()

    missionList = []
    for cmd in cmds:
        missionList.append(cmd)

    wpLastObject = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                           mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,
                           wp_Last_Latitude, wp_Last_Longitude, wp_Last_Altitude)

    missionList.append(wpLastObject)
    cmds.clear()
    for cmd in missionList:
        cmds.add(cmd)

    cmds.upload()
    return cmds.count

def ChangeMode(mode):
    global vehicle

    while vehicle.mode != VehicleMode(mode):
        vehicle.mode = VehicleMode(mode)
        time.sleep(0.1)

    return True


def  main_mission():
    global str_mode 
    global vehicle

    while True:
        if str_mode == 'GROUND':
            n_WP, missionList = get_current_mission()
            time.sleep(2)
            if n_WP > 0:
                print("A valid mission has been uploaded: takeoff!")
                str_mode = 'TAKEOFF'

        elif str_mode == 'TAKEOFF':
            add_last_waypoint_to_mission(vehicle.location.global_relative_frame.lat,
                                         vehicle.location.global_relative_frame.lon,
                                         vehicle.location.global_relative_frame.alt)
            print("Home waypoint added to the mission")
            time.sleep(1)
            arm_and_takeoff(10)

            # -- Change the UAV mode to AUTO
            print("Changing to AUTO")
            ChangeMode("AUTO")

            str_mode = 'MISSION'
            print("Switch mode to MISSION")


main_mission()
