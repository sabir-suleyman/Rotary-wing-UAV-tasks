## Bu Dosyayı başka dillerde oku:
<a href="README.md"><img src="https://img.shields.io/badge/-ENGLISH-red?style=for-the-badge"></a>
<a href="README.tr.md"><img src="https://img.shields.io/badge/-T%C3%9CRK%C3%87E-red?style=for-the-badge"></a>

# Repo Bilgisi
Bu repository döner kanat iha kategorisine ait bir aracın temel hareket (iniş-kalkış, sağ-sol, yukarı-aşağı) kodalarını, birkaç görev uygulama algoritmalarını içermektedir. 

# Simulasyon ortamı kurulumu
Aşağıda Ardupilot yazılımının ve Gazebo simulasyon ortamının Linux OS'a (Ubuntu 18.04 ve üzeri versiyonlarına) kurulumu adım adım belirtilmiştir:

1. İlk önce Terminali açıyoruz (Ctrl+Alt+T) ve şu komutları sırasıyla girerek **Ardupilot** için gerekli olan dosyaları indiriyoruz:
 ```
 sudo apt-get update
 ``` 
Kullanıcı şifresi isterse şifreyi girerek devam edebilirsiniz.

```
sudo apt-get install git
```

*Do you want to contuniue [Y/n]?* sorusuyla karşılaşacaksınız. `Enter` e basarak devam
edebilirsiniz.

```
sudo apt-get install gitk git-gui
```
*Do you want to contuniue [Y/n]?* sorusuyla karşılaşacaksınız. `Enter` e basarak devam
edebilirsiniz.

Devamında aşağıdaki komutları sırasıyla giriyoruz:

```
git clone https://github.com/your-github-userid/ardupilot
```

Bu işlem biraz uzun sürebilir.

Githubdan dosyayı indirdikten sonra ardupilot klasörüne gidiyoruz:

```
cd ardupilot
```

Daha sonra update işlemini gerçekleştiriyoruz:

```
git submodule update --init --recursive
```

İşlem bittikten sonra terminali kapatabiliriz.

Kapattıktan sonra görev çubuğundan `Files` e tıklayıp **Ardupilot** klasörünü buluyoruz. Klasöre sağ tıklayıp Terminalde açıyoruz.

Açtıktan hemen sonra:

```
Tools/environment_install/install-prereqs-ubuntu.sh -y
```

komutunu giriyoruz. Kullanıcı şifresini girerek devam ediyoruz.

Ardından

```
~/.profile
```

komutunu giriyoruz.

Artık Terminali kapatabiliriz. Kapattıktan sonra Oturumu kapatıp tekrardan giriyoruz (Restart da yapabilirsiniz)

Yeniden giriş yaptıktan sonra Terminali açıp **Ardupilot STİL** uygulamasını başlatıyoruz:

```
cd ardupilot/ArduCopter
```

Daha sonra

```
sim_vehicle.py -w
```

komutunu giriyoruz. İşlem bittikten sonra Ctrl+C yaparak komutu sonlandırıyoruz ve sonrasında

```
sim_vehicle.py --console --map
```

komutunu giriyoruz.

*MavProxy* ve *pymavlink* güncellemek için aşağıdaki komutu giriyoruz:

```
pip install --upgrade pymavlink MAVProxy --user
```

bittikten sonra artık Gazeboyu kurabiliriz.


# Gazebo Kurulumu

Komutları sırasıyla girerek Gazeboyu başarılı bir şekilde kurabilir ve ardupilotla
birlikte çalıştırabilirsiniz.

```
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
```

```
wget https://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
```

```
sudo apt update
```

```
sudo apt-get install gazebo9
```

```
sudo apt-get install libgazebo9-dev
```

```
git clone https://github.com/khancyr/ardupilot_gazebo
```

```
cd ardupilot_gazebo
```

```
mkdir build
```

```
cd build
```

```
cmake ..
```

```
make -j4
```

```
sudo make install
```

```
echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc
```

```
echo 'export GAZEBO_MODEL_PATH=~/ardupilot_gazebo/models' >> ~/.bashrc
```

```
. ~/.bashrc
```

Bu komutları başarılı bir şekilde gerçekleşdise demek ki Gazebo kurulmuştur. **Dikkat**: Eğer sanal makine kullanıyorsanız(*kullanmak tavsiye edilmez, onun yerine dual boot yapmayı tercih edebilirsiniz*) bu iki komutu girmeniz gerekecektir:

```
export SVGA_VGPU10=0
```
```
echo "export SVGA_VGPU10=0" >> ~/.bashrc
```

Eğer sanal makine kullanmıyorsanız (yani dual bootsa) bu komutları gözardı edebilirsiniz.

Şimdiyse:

```
Clear
```

Komutuyla terminali temizleyelim...

*Gazeboyu* ve *Ardupilot STİL*i başlatalım:

```
gazebo --verbose worlds/iris_arducopter_runway.world
```

Gazebo açılacaktır(ilk girdiğinizde baya uzun sürebilir). Açıldıktan sonra terminalde sol üst kısımdan File\New Tab yaparak yeni terminal
sayfası açıyoruz. Sırasıyla :

```
cd ~/ardupilot/ArduCopter
```

daha sonra ise:

```
../Tools/autotest/sim_vehicle.py -f gazebo-iris --console --map
```

Komutlarını giriyoruz.

Bu kadar...
