# SonoffSwitchControl

This is console menu application for actuating [Sonoff WIFI Smart Switch Basic](https://www.sonoff.in/index.php?route=product/product&path=62&product_id=75) by posting HTTP request written in Python. Your pc/laptop and Sonoff Smart Switches have to be on the same WiFi network and you need to know IP address for each of yours Sonoff Smart Switches. 

Number of switches are configurable trought `config.xml` file.

![Screenshot_from_2018-12-22_20-23-18](/uploads/32d11ca86f36d904a773edb0a7025be8/Screenshot_from_2018-12-22_20-23-18.png)

## Prerequisite
 * Python 3
 * setup and connected Sonoff WIFI Smart Switch Basic on your wifi network. How to is [HERE](https://www.letscontrolit.com/wiki/index.php/Tutorial_Arduino_Firmware_Upload#Download_and_installing_the_Arduino_IDE )

 ## Usage
In `config.xml` list all of yours Sonoff WIFI Smart Switches and they will appear in console menu. One switch is represented as a pair:
- `<name>`
- `<IP address>`.

 Start script as `python sonoff_switch_control.py`

## Conclusion
I used this script for testing my Sonoffs at the beginning. Now I run it on my Raspberry PI which I connect on IoT platform and control Sonnofs over my phone or Web.
