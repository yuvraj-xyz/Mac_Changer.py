#Change your Mac Address by Giving any Fake 12 Digit Mac Adress

import subprocess

interface = input("Interface (wlan0/eth0) > ")
new_mac = input("New Mac (XX:XX:XX:XX:XX:XX) > ")

print("[+] Change the Mac Adress of " + interface + " to " + new_mac + " : ")

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether "+ new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig " + interface , shell=True)
