#!/usr/bin/env python3
#
#       Sabir Süleymanlı <suleymanlisabir3@gmail.com>
#       
#       girilen_konuma_git.py            22.02.2022           
#       

from pickletools import float8
from dronekit import connect , VehicleMode , LocationGlobalRelative


drone = connect('127.0.0.1:14550', wait_ready=True)


iha = connect("127.0.0.1:14550", wait_ready= True)

def takeoff(irtifa1):

    while iha.is_armable is not True:

        print("Iha armedilebilir durumda degil...")
        
        
    print("Iha armedilebilir.")
            
            
    iha.mode = VehicleMode("GUIDED")
            
    print("Iha Guided moduna alindi.")

    iha.armed = True

    print("Iha basariyla arm edildi!")

    iha.simple_takeoff(irtifa1)

    while iha.location.global_relative_frame.alt < irtifa1*0.9:
        print("Iha Beirtilen yukseklige kalkiyor...")
    
    print("Iha istenilen irtifaya ulasti")

    
    


irtifa = int(input("Kalkilacak yukseklik degerini giriniz: "))

takeoff(irtifa)

konum = LocationGlobalRelative(-35.36237270,149.16512464,10)

iha.simple_goto(konum)
