import paramiko

def sshReboot(hostname,username="admin",password="",cmd="reboot"):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname.strip(),22,username,password,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print(stdout.readlines())
        print('%s OK\n'%(hostname))
        ssh.close()
        return True
    except :
        print('%s Error\n' %(hostname))
        print(stderr.read())
        return False
        

with open("./lists/client.txt","r") as ipList:
    for hostname in ipList.readlines():
        if sshReboot(hostname.strip(),"BYA","ampere2020."):
            print("Conected")
        else:
            print("Disconected")

"""for hostname in ipList.readlines():
    print(myping(hostname))
    response=os.system("ping -n 1 " + hostname)
    if response == 0:
        print("Status is up")
    else:
        print("Status is down")"""


#sshReboot("192.168.55.78")
