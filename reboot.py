import paramiko

def sshReboot(ip):
    username = "BYA"
    password = "ampere2020."
    cmd = "reboot"
    try:
        ssh = paramiko.SSHClient()
        
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,password,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        # stdin.write("Y") #interact with server, typing Y 
        print(stdout.read())
        # for x in stdout.readlines():
        # print x.strip("n")
        print('%s OK\n'%(ip))
        ssh.close()
    except :
        print('%s Error\n' %(ip))


ssh2("192.168.55.78")