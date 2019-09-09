#!/usr/bin/python3
"""
'
' This script only works for devices which are configured as describe here:
'	https://www.letscontrolit.com/wiki/index.php/Tutorial_Arduino_Firmware_Upload#Download_and_installing_the_Arduino_IDE 
'
' IMPORTANT: configure ARDUINO IDE as it presented here: https://imgur.com/SRXAIEH
'
' Before starts script insert parameters in config.xml file
"""
import time
import sys
import socket
import requests

import xml.etree.ElementTree as ET


def get_current_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("\t" + s.getsockname()[0])
    s.close()


def sonoff_switch(ip_add, value):
    base_url = "http://" + ip_add + "/control?cmd=event,Turn"
    if value == 1 or value == "true":
        base_url = base_url + "On"
    else:
        base_url = base_url + "Off"

    payload = {}
    try:
        response = requests.post(base_url, data=payload)
    except:
        print("Couldn't change switch state")
        return False

    print(response.text)  # TEXT/HTML
    print(response.status_code, response.reason)  # HTTP

    return True


def main():
    print(
        "--------------------------------------------------------------\n\r\tThis is Console App for Sonoff HTTPS request\n\r--------------------------------------------------------------\n\rYour current IP add is:"
    )
    get_current_ip()

    tree = ET.parse("config.xml")
    root = tree.getroot()

    number_of_children = len(root.getchildren())

    while 1:
        print("\n\rSelect from menu:\n\r-------------------")
        for x in range(0, number_of_children):
            print(str(2 * x) + ")" + root[x][0].text + " ON")
            print(str(2 * x + 1) + ")" + root[x][0].text + " OFF")
        print("q)Quit")

        var = input(">>")
        if var == "q":
            print(
                "\tQuit App\n\r--------------------------------------------------------------"
            )
            sys.exit()

        # TODO: True and False
        var = int(var)
        if var > 2 * number_of_children - 1:
            print("\tUndefined Selected. Retype")
            continue

        # TODO: parni su ON, neparni su OFF
        if var % 2 == 0:
            new_var = var / 2
            value = 1
        else:
            value = 0
            new_var = round((var - 1) / 2, 0)
        new_var = int(new_var)

        print(root[new_var][0].text + " selected")
        if sonoff_switch(root[new_var][1].text, value):
            print("\tSucessfully")
            continue
        else:
            print("\tFailed")
            continue


if __name__ == "__main__":
    main()
