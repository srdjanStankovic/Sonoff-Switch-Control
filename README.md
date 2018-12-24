# SonoffSwitchControl

This is console menu application for actuating [Sonoff WIFI Smart Switch Basic](https://www.sonoff.in/index.php?route=product/product&path=62&product_id=75) by posting HTTP request written in Python. Your pc/laptop and Sonoff Smart Switches have to be on the same WiFi network and you need to know IP address for each of yours Sonoff Smart Switches. 

Number of switches are configurable trought `config.xml` file.

![Screenshot_from_2018-12-23_13-26-04](/uploads/83a68bb90c6f263417ba0d4ff99abb49/Screenshot_from_2018-12-23_13-26-04.png)

## Prerequisite
 * Python 3
 * setup and connected Sonoff WIFI Smart Switch Basic on your wifi network. How to is [HERE](https://www.letscontrolit.com/wiki/index.php/Tutorial_Arduino_Firmware_Upload#Download_and_installing_the_Arduino_IDE ). **IMPORTANT:** setup Arduino IDE Settings like [THIS](https://imgur.com/SRXAIEH)

 ## Usage
In `config.xml` list all of yours Sonoff WIFI Smart Switches and they will appear in console menu. One switch is represented as a pair:
- `<name>`
- `<IP address>`.

 Start script as `python sonoff_switch_control.py`

## Conclusion
I used this script for testing my Sonoffs at the beginning. Now I run it on my Raspberry PI which I connect on IoT platform and control Sonnofs over my phone or Web.
