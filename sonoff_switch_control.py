#!/usr/bin/python
'''
'
' This script only works for devices which are configured as describe here:
'	https://www.letscontrolit.com/wiki/index.php/Tutorial_Arduino_Firmware_Upload#Download_and_installing_the_Arduino_IDE 
'
' IMPORTANT: configure ARDUINO IDE as it presented here: https://imgur.com/SRXAIEH
'
' Before starts script insert parameters in config.xml file
'''
import time
import sys
import socket
import requests

#TODO: * add requirements.txt file
#      * import python logger

def get_current_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	print(s.getsockname()[0])
	s.close()

def sonoff_switch(ip_add, value):
	base_url="http://"+ ip_add + "/control?cmd=event,Turn"
	if value==1 or value=='true':
		base_url=base_url+"On"
	else:
		base_url=base_url+"Off"

	payload = {}
	try:
		response = requests.post(base_url, data=payload)
	except:
		print("Couldn't change switch state")
		return False

	print(response.text) #TEXT/HTML
	print(response.status_code, response.reason) #HTTP

	return True


def main():
	print("--------------------------------------------------------------\n\r\tThis is Console App for Sonoff HTTPS request\n\r--------------------------------------------------------------\n\r")
	get_current_ip()

	while 1:
		print("\n\rSelect from menu:\n\r-------------------\n\r1)LED-strip-ON\n\r2)LED-strip-OFF\n\r3)OurLamp-ON\n\r4)OurLamp-OFF\n\rq)quit")

		var = raw_input(">>")
                #TODO: generic made a list from .xml files
		if var=='1':
			print("\tOurLamp-ON")
			if sonoff_switch("192.168.0.14", 1):
				print("\tSucessfully")
				continue
			else:
				print("\tFailed")
				continue
		elif var=='2':
			print("\tOurLamp-OFF")
			if sonoff_switch("192.168.0.14", 0):
				print("\tSucessfully")
				continue
			else:
				print("\tFailed")
				continue
		if var=='3':
			print("\tLED-strip-ON")
			if sonoff_switch("192.168.0.15", 1):
				print("\tSucessfully")
				continue
			else:
				print("\tFailed")
				continue
		elif var=='4':
			print("\tLED-strip-OFF")
			if sonoff_switch("192.168.0.15", 0):
				print("\tSucessfully")
				continue
			else:
				print("\tFailed")
				continue
		elif var=='q':
			print("\tQuit App")
			sys.exit()
		else:
			print("\tUndefined Selected -> Exit")


if __name__ == "__main__":
    main()