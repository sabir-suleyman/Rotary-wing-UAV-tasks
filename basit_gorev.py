#!/usr/bin/env python3
#
#       Sabir Süleymanlı <suleymanlisabir3@gmail.com>
#       
#       basit_gorev.py            05.07.2022           
#       


#en son bunu yaptim

from dronekit import Command ,connect , VehicleMode, LocationGlobalRelative
import time
from pymavlink import mavutil


iha = connect("127.0.0.1:14550", wait_ready= True)


def takeoff(irtifa1):

    while iha.is_armable is not True:
        print("Iha armedilebilir durumda degil...")
        
        
    print("Iha armedilebilir.")
            
            
    iha.mode = VehicleMode("GUIDED")
            
    print("Iha Guided moduna alindi.")

    iha.armed = False

    print("Iha basariyla arm edildi!")

    iha.simple_takeoff(irtifa1)

    while iha.location.global_relative_frame.alt <= irtifa1*0.9:
        print("Iha Beirtilen yukseklige kalkiyor...")
        time.sleep(1)
    
    print("Iha istenilen irtifaya ulasti")

#irtifa = int(input("Kalkilacak yukseklik degerini giriniz: "))


def gorev_ekle():
    
    # Global bir degisken olarak tanimladim
    global komut
    
    # Drona komut yollayabilmek  icin kullanilir
    komut = iha.commands

    # Dronumuzda halihazirda bir gorev varsa onu siler
    komut.clear()
    time.sleep(1)

    #  "komut.add()" Dronumuza herhangi bir gorev ekleyebilmemizi sagliyor
    # Bir adet girdi aliyor(Command() seklinde) bu 
    # drona gonderecegimiz komutu belirliyor

    # Dorduncu parametreye (x,y,z) yi neye gore referans 
    # aldigimizi yazmamizi istiyor 

    # Besinci parametre drona gonderecegimiz komutun
    # ne oldugunu belirten parametre
    # (Genellikle ilk komut MAV_CMD_NAV_TAKEOFF olmali)
    # Boylelikle 60.satirdaki komutumuz TAKEOFF yapiyor
    komut.add(Command(0,0,0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,0,10))
    

    # Simdi yazacamiz komut ise dronumuzun gitmesini istedigimiz yer olacak
    # 70.satirdaki komut WAYPOINT 

    # mavutil.mavlink.MAV_CMD_NAV_WAYPOINT den sonra gelecek parametre delaydir.
    # Dronun gidecegi konumda ne kadar sure kalmasini girebiliriz
    # Durmasini istemiyorsak 0 verebiliriz
    
    # 70.satirdaki komut Dronu belirttigimiz 1.konuma goturur (irtifayi 20 metreye cikartiyor)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36318940,149.16530440,10))
    

    # Dronu 2.konuma goturen komut satiri (irtifayi 30 metreye cikartiyor ayni zamanda)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36314010,149.16521250,10))
    
    # Dronu 3.konuma goturen komut satiri (irtifayi 30 metreye cikartiyor ayni zamanda)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36309800,149.16511660,10))

    # Dronu 4.konuma goturen komut satiri (irtifayi 30 metreye cikartiyor ayni zamanda)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36303510,149.16519780,10))

    # Dronu 5.konuma goturen komut satiri (irtifayi 30 metreye cikartiyor ayni zamanda)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36308050,149.16529900,10))

    # Dronu 6.konuma goturen komut satiri (irtifayi 30 metreye cikartiyor ayni zamanda)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,-35.36320190,149.16513540,10))

    # RTL komutu. Aracin kalktigi yere geri donmesini saglayan komut
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0))
    

    # Dogrulama amacli yukaridaki komutun kopyasi
    # (Anlami yok)
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0))
    
    # Gonderecegimiz komutlari yazdiktan sonra komut.upload() ile 
    # yazdigimiz komutlari Drone yukluyoruz
    komut.upload()

    print("Komutlar Yukleniyor...")
    

irtifa = int(input("Kalkilacak yukseklik degerini giriniz: "))    
takeoff(irtifa)

gorev_ekle()


# Aracin sonraki komutunu 0 yapar (Bir karisiklik olmamasi acisindan) 
komut.next = 0

# Dron boylesine hazir komutlari calistirabilmek icin 
# AUTO moduna alinmasi gerekir
iha.mode = VehicleMode("AUTO")


# Buradaki amac sonsuz dongu olusturmak ve 
# Dron son komutu calistirdiktan sonra dongu kirilacak

while True:
    next_waypoint = komut.next
    print("Siradaki komut",next_waypoint)
    time.sleep(1)

    if next_waypoint is 7:
        print("Gorev Bitti..")
        break

print("Donguden cikildi....")
