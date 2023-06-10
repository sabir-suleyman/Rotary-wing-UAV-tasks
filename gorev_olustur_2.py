#!/usr/bin/env python3
#
#       Sabir Süleymanlı <suleymanlisabir3@gmail.com>
#       
#       gorev_olustur_2.py            15.07.2022           
#       

from dronekit import Command,connect , VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil

vehicle = connect("127.0.0.1:14550", wait_ready= True)

def gorevi_temizle():
    global vehicle

    cmds = vehicle.commands
    cmds.clear()
    cmds.upload()


def gorevi_indir():
    global vehicle

    cmds = vehicle.commands
    cmds.download()
    cmds.wait_ready()



def gorevi_al():
    print("Downloading mission")
    gorevi_indir()
    missionList = []
    n_WP = 0
    for wp in vehicle.commands:
        missionList.append(wp)
        n_WP += 1

    return n_WP, missionList




def gorevi_guncelle(wp_Last_Latitude, wp_Last_Longitude, wp_Last_Altitude):
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


def arm_and_takeoff (altitude):
    global vehicle

    while not vehicle.is_armable:
        print("arm edilmesini bekle")
        time.sleep(1)

    print("Arm edildi")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    while not vehicle.armed: time.sleep(1)
    print("Takeoff")
    time.sleep(2)
    vehicle.simple_takeoff(altitude)
    while True:
        altitude2 = vehicle.location.global_relative_frame.alt
        print(">> Altitude = %.1f m" % altitude2)
        if altitude >= altitude - 1:
            print("irtifaya ulasildi ")
            break
        time.sleep(1)



def mod_degistirme(mode):
    global vehicle

    while vehicle.mode != VehicleMode(mode):
        vehicle.mode = VehicleMode(mode)
        time.sleep(0.1)

    return True



vehicle.mode = VehicleMode("AUTO")
mod_degistirme("AUTO")
gorevi_temizle()
gorevi_indir()
gorevi_guncelle()
arm_and_takeoff(10)
