#!/usr/bin/env python

import subprocess
interface = 'wlan0'
new_macAddress = '11:22:33:44:99'
subprocess.call("ifconfig" , shell=True)
subprocess.call("ifconfig"+ interface + "hw ether" + new_macAddress , shell=True)
subprocess.call("ifconfig wlan0 up" , shell=True)

