#####################################
## QR-CODE GUEST WIFI WLAN
#####################################
# library for handling mathematical operations & arrays
import numpy as np
# for image processing & qrcode display 
import cv2
# library for creating WiFi access point on Raspberry-Pi
from PyAccessPoint import pyaccesspoint
# library for timing and scheduling 
import time
# library for system variable accessing and using raspbian-linux shell output
import subprocess
# for QR-code generation and saving in appropriate formats
import pyqrcode
# for getting and working with linux terminal and output provision
import os


def run():
    # start time variable 
    start = time.time()

    # provide the name of your ssid
    ssid = 'YALEFox_Guest_WiFi'  # yale fox; the person to whom idea is inspired and all credited goes to him

    # give the wifi protocol segment to be implemented    
    Wifi_Protocol = 'WPA/WPA2'

    # wpa_passphrase generation using builtin "urandom" linux program and save it
    # or you can enter it as for any length from 8 to 64 characters through "wpa_passphrase" variable
    # like wpa_passphrase = 'ajkdsbdjasdbasjkflfdkalshdaskdhasldkasld78'
    wpa_passphrase = subprocess.getoutput('< /dev/urandom tr -cd "[:print:]" | head -c 63;')

    # creating the accesspoint object "ap" from the class of pyaccesspoint module
    ap = pyaccesspoint.AccessPoint()

    # provide your desired ssid and assign it to access point object "ap"
    ap.ssid = ssid

    # creating passphrase (password) and assiging it to access point object "ap"
    ap.password = wpa_passphrase

    # provide the network ip which needs to be implemented for WiFi LAN (default ip = 192.168.45.1)
    ap.ip = "192.168.4.1"

    # ipv4 forwarding and bridging internet access when eth0 is accessing internet for raspberry pi
    # "eth0" is used as internet packet forwarding and making accesspoint as internet accessible
    ap.inet = "eth0"

    # run the "ap" object so that the access point is created on the RPI with desired above mentioned info 
    ap.start()

    # supplemnetary printing of object location
    print(ap)

    # providing true value gives "ap" successfully created and implemented and useful
    # while on False check the manual and procedure accordingly
    print(ap.is_running())

    # time value for how much long to be "ap" should be created and maintained (in secs)
    time_value = 86400   # 2 min = 120 secs  | 24 hrs = 86400 secs | 7 days = 604800 secs

    # Generate QR code picture for Android
    aqrcode = pyqrcode.create(F'WIFI:S:{ssid};T:{Wifi_Protocol};P:{wpa_passphrase};;')

    # save the qrcode in png format
    aqrcode.png(r'/home/pi/QRcode-Guest-WiFi/qrcode/aqrcode.png', scale=2)

    # IOS requires a hosted webpage which I do not want to host
    # Use the copy to clipboard function for the password and manually connect instead.
    iqrcode = pyqrcode.create(F'${wpa_passphrase}')

    # save the qrcode in png format
    iqrcode.png(r'/home/pi/QRcode-Guest-WiFi/qrcode/iqrcode.png', scale=2)

    # create a black image on which qrcodes will lie on (it must of resolution as of LCD-screen)
    black = np.zeros((320, 480, 3), 'uint8')

    # locate and load the qrcode-image of android to "qr-android" variable
    qr_android = cv2.imread(r'/home/pi/QRcode-Guest-WiFi/qrcode/aqrcode.png')

    # locate and load the qrcode-image of iphone to "qr-iphone" variable    
    qr_iphone = cv2.imread(r'/home/pi/QRcode-Guest-WiFi/qrcode/iqrcode.png')    

    # shape of black image (320x480)
    x1 = black.shape[0]
    y1 = black.shape[1]

    # shape of android qr-code 
    x2 = qr_android.shape[0]
    y2 = qr_android.shape[1]

    # shape of iphone qr-code
    x3 = qr_iphone.shape[0]
    y3 = qr_iphone.shape[1]

    # finding center of black image
    a = int((x1-x2)/2)
    b = int((y1-y2)/2)

    # make a copy of black image from "black" to "res"
    res = black.copy()

    # pasting images of qr-code of android and iphone to the black-image for display
    res[a:a+x2, b-50:b+y2-50] = qr_android
    res[a:a+x3, b+100:b+y3+100] = qr_iphone

    # providing font-text style
    font = cv2.FONT_HERSHEY_SIMPLEX

    # ssid and wpa_passphrase texts to be put on the top of the black image for display 
    cv2.putText(res, f'WLAN-SSID = {ssid}', (b-20,a-50), font, 0.4, (255,255,255), 1)
    cv2.putText(res, f'WLAN-Paraphrase = {wpa_passphrase}', (b-130,a-20), font, 0.4, (255,255,255), 1)

    # label texts to be put on bottom each of the qr-codes according to their types
    txt1 = 'Android'
    txt2 = 'Iphone'
    cv2.putText(res, f'{txt1}', (b-30,a+140), font, 0.4, (255,255,255), 1)
    cv2.putText(res, f'{txt2}', (b+125,a+120), font, 0.4, (255,255,255), 1)

    # save the output for making it as a screen saver for displaying it over touch LCD-screen
    cv2.imwrite(r'/home/pi/QRcode-Guest-WiFi/output/output.png', res)

    # screen saver program running it through "feh module"
    os.popen("feh -Z -z -x -F --hide-pointer /home/pi/QRcode-Guest-WiFi/output/")
        
    # looping for timing the "ap" for a certain schedule
    while(True):
        # elasped time is the variable after accesspoint is created and maintain for that much long
        elasped = time.time() - start
        # conditional statement for "ap" time up scheduling
        if(elasped > time_value):
            print('time up.!')
            # this command stop the access point "ap" and close the connection of WiFi LAN
            ap.stop()
            # break and goes off the program, to terminate it as whole 
            # and run it again as recursively
            run()

if __name__ == "__main__":
    run()