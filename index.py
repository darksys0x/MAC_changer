#!/usr/bin/env python

import subprocess
import optparse



def argument():
    parsr = optparse.OptionParser()
    parsr.add_option("-i", "--interface", dest="interface", help="add interface")
    parsr.add_option("-m","--mac", dest="new_mac", help="add new mac")
    (option, argument) = parsr.parse_args()
    if not option.interface:
        parsr.error("[-] plese spicfic interface")
    elif not option.new_mac:
        parsr.error("[-] please spisfic new mac")
    return option




def change_mac(interface, new_mac):
    print("[+] change interface of "+interface+" and new mac is "+new_mac)
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig", interface,"hw","ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])





option = argument()
change_mac(option.interface,option.new_mac)










