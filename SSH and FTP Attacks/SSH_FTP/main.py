'''                                         '''

    ########################################
    #         SSH and FTP Attacks          #
    #       Ahmad Reza Parsi Zadeh         #
    #        github: ahmad-reza-ut         #
    ########################################

'''                                         '''
'''
            Important Notes:
    

'''
#------------- Returning banner from a port -------------#
# Importing necessary libraries
import pexpect

PROMPT = ['#', '>>>', '>', '\$']
#------------ Connect function --------------#
def connect(HOST, USERNAME, PASSWORD):
    ssh_newkey = 'Are you sure you want to continue connecting? '
    Connect_SSH_String = 'ssh' + USERNAME + '@' + HOST
    child = pexpect.spawn(Connect_SSH_String)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error connecting')
            return
    child.sendline(PASSWORD)
    child.expect(PROMPT)
    return child
# ------------ Send_Command function --------------#
def send_command(child, Command):
    child.sendline(Command)
    child.expect(PROMPT)
    print(child.before)
#------------ Main function --------------#
def main():
    HOST = input("Enter the IP Address: ")
    USERNAME = input("Enter the Username: ")
    PASSWORD = input("Enter the Password: ")
    CONNECTION = connect(HOST, USERNAME, PASSWORD)
    Command = input("Write any command to run: ")
    send_command(CONNECTION, Command)

#--------------------------#
if __name__ == '__main__':
    main()

#------------ END --------------#