from urllib import response
import paramiko,os

def sshReboot(ip):
    username = "BYA"
    password = "ampere2020."
    cmd = "reboot"
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,username,password,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print(stdout.read())
        print('%s OK\n'%(ip))
        ssh.close()
    except :
        print('%s Error\n' %(ip))
        print(stderr.read())

ipList=open("./lists/client.txt", "r")
ipList.seek(0)

for hostname in ipList.readlines():
    response=os.system("ping -n 1 " + hostname)
    if response == 0:
        print("Status is up")
        sshReboot(hostname)
    else:
        print("Status is down")


#sshReboot("192.168.55.78")
