#Change your Mac Address by Giving any Fake 12 Digit Mac Address

import subprocess
import optparse
import re

def get_arguements():
    parser = optparse.OptionParser()
    parser.add_option("-i" , "--interface", dest="interface", help="Interface to Change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Adress")
    (options, arguements) = parser.parse_args()
    if not options.interface:
        options.error("[-] Please Specify an Interface to Continue, --help for more Info ")
    elif not options.new_mac:
        options.error( " [-] Please Specify an New Mac to Continue, --help for More Info ")
    return options

def change_mac(interface, new_mac):
    print("[+] Change the Mac Address of " + interface + " to " + new_mac + " : ")

    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether "+ new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group()
    else:
        print("[-] Could not Read Mac Address ")

options = get_arguements()
current_mac = get_current_mac(options.interface)
print("Current Mac = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac Address Successfully Changed to " + current_mac)
else:
    print("[-] Mac Address Did not get Changed.")
