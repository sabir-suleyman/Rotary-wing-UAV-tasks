from dronekit import connect , VehicleMode, LocationGlobalRelative
import time

iha = connect("127.0.0.1:14550", wait_ready= True)


# Iha armedilebilir durumda mi? True ya da False dondurur
print(iha.is_armable)


# Iha armed durumunda mi? True ya da False dondurur
print(iha.armed)

# Ihanin modunu Guided yapar
iha.mode = VehicleMode("GUIDED")

# Ihanin anlik irtifasi (deniz seviyesinden)
print(f'Irtifa:{iha.location.global_relative_frame.alt} ')


# Ihani arm eder ve verilen deger kadar yukariya tasir
iha.simple_takeoff(10)



# Ihanin ilk once armedilebilir durumda olup olmadigina bakan
# daha sonra eger armedilebilirse guided moduna alan 
# ve daha sonra arm edip girilen metre yukseklige 
# ulasmasini saglayan fonksiyon

def takeoff(irtifa):

    # Oncelikle durumumuz armedilebilir durumda olup olmadigini kontrol ediyoruz
    while iha.is_armable:

        print("Iha armedilebilir.")
        
        # Iha disaridan gelen komutlari uygulayabilsin diye modu Guided'e aliyoruz
        iha.mode = VehicleMode("GUIDED")
        
        print("Iha Guided moduna alindi.")

        iha.armed = True

        print("Iha arm edildi!")

        iha.simple_takeoff(irtifa)
        time.slepp(1)
        print("Iha hedefe dogru gidiyor...")
        break
    
    print("Iha armedilebilir durumda degil!")

takeoff(10)

# Konum fonksiyonu. 3 parametre alir: {lat,lon,alt} {enlem,boylam,irtifa}
konum = LocationGlobalRelative(-35.36257282 , 149.16513083 , 20)

# Ihani konuma dogru goturen fonksiyon
iha.simple_goto(konum)

#Drona Komut yollayabilmek icin kullanilir
komut = iha.commands


#Droneda halihazirda herhangi gorev varsa onu drondan siliyor
komut.clear()

#Drona herhangi bir gorev ekleyebilmemizi sagliyor
komut.add()
