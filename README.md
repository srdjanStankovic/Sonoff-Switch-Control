# Sonoff-Switch-Control

This is console menu application for actuating [Sonoff WIFI Smart Switch Basic](https://www.sonoff.in/index.php?route=product/product&path=62&product_id=75) by posting HTTP request written in Python. Your pc/laptop and Sonoff Smart Switches have to be on the same WiFi network and you need to know IP address for each of yours Sonoff Smart Switches(you will know by following procedure below). 

## Prerequisite
 * Python 3
 * Connect Sonoff WIFI Smart Switch Basic on your WiFi network. How to is [HERE](https://www.letscontrolit.com/wiki/index.php/Tutorial_Arduino_Firmware_Upload#Download_and_installing_the_Arduino_IDE ). **IMPORTANT: You will actually write new firmware to Sonoff. Setup Arduino IDE Settings like [THIS](https://imgur.com/SRXAIEH).**
 * Configure Sonoff WIFI Smart Switch Basic following ***Sonoff configuration*** section from [THIS](https://rutg3r.com/sonoff-firmware-tutorial-to-esp-easy/) guide.
 
 ## Usage
In `config.xml` list all of yours Sonoff WIFI Smart Switches and they will appear in console menu. One switch is represented as a pair:
- `<name>`
- `<IP address>`.

 Start script as `python sonoff_switch_control.py` and console like on the picture below will appear. For every listed switch ON and OFF option will be presetned in the list.

 <img width="426" align="middle" alt="capture" src="https://user-images.githubusercontent.com/8199494/51274476-9a599e80-19cf-11e9-8f9d-49153a14d0d2.PNG">

## Conclusion
I used this script for testing my Sonoffs at the beginning. Now, I run it on my Raspberry PI which I connect on IoT platform and controls Sonnofs over my phone or web remotely.
