#!/usr/bin/env python

import subprocess
interface = input('interface > ')
new_macAddress = input('new MAC > ')

print('[+] Chinging MAC address for '+ interface + ' to '+ new_macAddress)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_macAddress])
subprocess.call(['ifconfig', interface, 'up'])



#############-----
