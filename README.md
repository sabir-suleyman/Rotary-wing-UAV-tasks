## Read this File in other languages:
<a href="README.md"><img src="https://img.shields.io/badge/-ENGLISH-red?style=for-the-badge"></a>
<a href="README.tr.md"><img src="https://img.shields.io/badge/-T%C3%9CRK%C3%87E-red?style=for-the-badge"></a>

# Repo Info
This repository contains the basic motion (landing-takeoff, right-left, up-down) codes of a vehicle belonging to the rotary wing UAV category, as well as several mission execution algorithms. 

# Simulation environment setup
Below is the step-by-step installation of Ardupilot software and Gazebo simulation environment on Linux OS (Ubuntu 18.04 and above):

1. First, open the Terminal (Ctrl+Alt+T) and download the necessary files for **Ardupilot** by entering the following commands in order:
 ```
 sudo apt-get update
 ``` 
If it asks for a user password, you can enter it and continue.

```
sudo apt-get install git
```

You will see the question *Do you want to contuniue [Y/n]?*. Continue by pressing `Enter`
you can.

```
sudo apt-get install gitk git-gui
```
You will see the question *Do you want to contuniue [Y/n]?*. Continue by pressing `Enter`
you can.

Then we enter the following commands in order:

```
git clone https://github.com/your-github-userid/ardupilot
```

This process may take a while.

After downloading the file from Github, we go to the ardupilot folder:

```
cd ardupilot
```

Then we perform the update process:

```
git submodule update --init --recursive
```

After the process is finished, we can close the terminal.

After closing, click on `Files` from the taskbar and find the **Ardupilot** folder. Right click on the folder and open it in Terminal.

Immediately after opening it:

```
Tools/environment_install/install-prereqs-ubuntu.sh -y
```

We enter the command. We continue by entering the user password.

Then we enter

```
~/.profile
```

command.

Now we can close the terminal. After closing, we log out and log in again (you can also Restart)

After logging in again, we open the Terminal and start the **Ardupilot STYLE** application:

```
cd ardupilot/ArduCopter
```

Afterwards

```
sim_vehicle.py -w
```

command. After the process is finished, end the command by Ctrl+C and then

```
sim_vehicle.py --console --map
```

We enter the command

To update *MavProxy* and *pymavlink* we enter the following command:

```
pip install --upgrade pymavlink MAVProxy --user
```

After it is finished, we can now install the Gazebo.


# Gazebo Installation

By entering the commands in order, you can successfully set up the Gazebo and use ardupilot
you can run it together.

```
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
```

```
wget https://packages.osrfoundation.org/gazebo.key -O - | | sudo apt-key add -
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
cmake..
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

If these commands were executed successfully, then Gazebo is installed. **Warning: If you are using a virtual machine (*not recommended, you can choose to dual boot instead*) you will need to enter these two commands:

```
export SVGA_VGPU10=0
```
```
echo "export SVGA_VGPU10=0" >> ~/.bashrc
```

If you are not using a virtual machine (i.e. dual boot) you can ignore these commands.

Now:

```
Clear
```

Let's clear the terminal with the command...

Let's start *Gazeboyu* and *Arrdupilot STYLE*:

```
gazebo --verbose worlds/iris_arducopter_runway.world
```

Gazebo will open (it may take a long time the first time you enter). Once it is open, you can create a new terminal by going to File\New Tab in the top left of the terminal.
page. In order :

```
cd ~/ardupilot/ArduCopter
```

and then:

```
../Tools/autotest/sim_vehicle.py -f gazebo-iris --console --map
```

We enter the commands.

That's it...
