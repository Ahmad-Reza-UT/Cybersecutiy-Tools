'''                                         '''

    ########################################
    #         ARP Spoofer Script           #
    #       Ahmad Reza Parsi Zadeh         #
    #        github: ahmad-reza-ut         #
    ########################################

'''                                         '''
'''
            Important Notes:
        In this project since we are using an infinite while
        loop, so i suggest you to run this program in linux by 
        using command line  and there you will be able to interrupt 
        or end the execution by Crtl+C combinational key.
'''

#------------- ARP Spoofer -------------#
# Importing necessary libraries
from Imports import *

#------------------ Main ------------------#
def main():
    try:
        SOCKET = socket.socket(socket.AF_PACKET, socket.SOCK_RAW. socket.ntohs(0x0003))
    except:
        print(colored("[!!] Error on creating socket object:(", 'red'))
        while True:
            packet = SOCKET.recvfrom(65535)
            packet = packet[0]
            ether_length = 14
            ether_header = packet[:ether_length]

            ethernet = unpack('!6s6sH', ether_header)
            ether_protocol = socket.ntohs(ethernet[2])
            print('[+] Destination MAC: \t' + ether_address(packet[0:6]) +
                  '\n[+] Source MAC: \t ' + ether_address(packet[6:12]) +
                  '\n[+] Protocol: \t' + str(ether_protocol))

# ---------------------------- #
def ether_address(a):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x"%(ord(a[0]), ord(a[1]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b
# ---------------------------- #
if __name__ == "__main__":
    main()

#---------------- END ----------------#