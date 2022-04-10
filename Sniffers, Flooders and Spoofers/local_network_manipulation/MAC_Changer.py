'''                                         '''

    ########################################
    #         Mac Changer Script           #
    #       Ahmad Reza Parsi Zadeh         #
    #        github: ahmad-reza-ut         #
    ########################################

'''                                         '''

'''
            Important Notes:
        This program works for Linux Command Line Interface.
        All of the commands will send to bash with subprocess.

'''

#------------- Mac Changer -------------#
# Importing necessary libraries
from Imports import *

#------------------ Main ------------------#
def main():
    interface = input("[+] Enter an interface to change its MAC Address: ")
    new_mac_address = input("[+] Enter the MAC Address you want to put: ")
    before_change = subprocess.check_output(["ifconfig", interface])
    mac_change(interface, new_mac_address)
    after_change = subprocess.check_output(["ifconfig", interface])

    if before_change == after_change:
        print(colored("[-] Failed to change the MAC Address:(", 'red'))
    else:
        print(colored("[+] MAC Address changed to: " + new_mac_address + "On Interface" + interface, 'green'))

#-------------- MAC Changer function --------------#
def mac_change(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
# ----------------------------#
# ----------------------------#
if __name__ == "__main__":
    main()

#---------------- END ----------------#