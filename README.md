# QRcode-Guest-WiFi
## Raspberry-Pi based QR-code Guest WiFi access point (AP)

![image](https://github.com/HarisFateh/QRcode-Guest-WiFi/blob/master/RaspWlan.jpg)


### QR-code Guest WiFi: (Implementation)

#### 1. Get ready your Raspberry-Pi(RPI), (tested with Raspberry-Pi 3-B)

- Download the latest version of Raspbian via link: https://www.raspberrypi.org/downloads/raspbian/
- Install the downloaded version using "Etcher" or "Win32DiskImager" on the inserted SD-card. (note: make sure SD-card is properly formatted and size above 8 GB)
- Etcher provides easy to install 3 steps. Etcher downloading link: https://www.balena.io/etcher/
- You can connect it via "SSH" or "VNC" by enabling both modes. Easier way is to connect with HDMI port
  For remote desktop access enable "VNC" and install: "sudo apt-get install xrdp" in raspbian terminal 	
- Now you are on the screen of the Raspbian either with Desktop or with terminal 
- Connect with an Internet connection through WiFi or Ethernet Port

- [Reference for RPI-ssh making accessible](References/RPI-SSH.txt)

- [Reference for ethernet sharing](References/Ethernet bridge sharing.docx)

- [Reference for tft lcd screen 3.5 inch making work](References/RPI-TFT LCD Screen.txt)

- [Reference for building python opencv manually](References/building openCV.txt)

- [Reference for libraries](References/libraries required.txt)


#### 2. Preparation

- Open the terminal & run:
```
sudo raspi-config
```
  Navigate to "Advanced Options" & select Expand Filesystem

- Now once the RPI is ready with latest version of Raspbian (buster-image) run the following commands:

```
sudo apt-get update
sudo apt-get upgarde
```

#### 3. Setting up LCD-screen (RPI 3.5 inch TFT Touch Screen, SPI)

- Open the terminal and type:
```
sudo raspi-config
```
Navigate to Interfacing options and enable "SPI" mode as well
- Connect the LCD-screen with RPI
- For setting up touch Screen run following commands on terminal:
```
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./LCD35-show
```
- RPI is now reboot itself and then you can see the screen goes to desktop mode

#### 4. Libraries to be installed prior to run application (we utilize python3)

- Run following commands to install the desired libraries in your RPI;

- for pyaccesspoint library:
```	
sudo apt install python3-dev python3-pip && sudo pip3 install wireless netifaces psutil
sudo apt update && sudo apt --yes --force-yes install dnsmasq hostapd python3-dev python3-pip && sudo pip3 install pyaccesspoint
sudo pip3 install packaging
```	
Recommended: run the following commands only once on the terminal for testing access-point formation:
 sudo pyaccesspoint start
 
(now make sure the access point is appeared, check it by watching the WiFi Hotspot list on your phone with name of "MyAccesspoint")
  sudo pyaccesspoint stop

- for pyqrcode library:
```
pip3 install pyqrcode
pip3 install pypng
```
- for opencv library:
```
pip3 install opencv-python
pip3 install opencv-contrib-python
```
- for screen saver library:
```
sudo apt-get install feh
sudo apt-get install xscreensaver
```

#### 5. Making Screen saver work

- you need to set the console blanking. The current setting, in seconds, can be displayed using
```
cat /sys/module/kernel/parameters/consoleblank
```
- Here, consoleblank is a kernel parameter. In order to be permanently set, it needs to be defined on the kernel command line.

```
sudo nano /boot/cmdline.txt
```
- Add consoleblank=0 to turn screen blanking off completely, or edit it to set the number of seconds of inactivity before the console will blank. Note the kernel command line must be a single line of text.

#### 6. Last Step

- Now simply run the following python file in the terminal:

```
sudo python3 guest-wlan.py
```

#### now you get the output as expected..!!
Enjoy and Fork please..!!
