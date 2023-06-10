#!/usr/bin/env python3
#
#       Sabir Süleymanlı <suleymanlisabir3@gmail.com>
#       
#       girilen_irtifaya_kalk.py            22.02.2022           
#       

from dronekit import connect , VehicleMode
import time

iha = connect("127.0.0.1:14550", wait_ready= True)

def takeof(irtifa1):

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
        time.sleep(1)
    
    print("Iha istenilen irtifaya ulasti")

irtifa = int(input("Kalkilacak yukseklik degerini giriniz: "))

takeof(irtifa)
