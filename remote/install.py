
import os
import time
import sys
import paramiko

host = '198.154.99.129'
user = 'nashwin'
password = 'hiSweden19'
command = 'date'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=host, username=user, password=password)
#shell = ssh.invoke_shell()

#shell.send(command + "\n")

stdout = ssh.exec_command(command)
output = []
for line in stdout:
    print (line)

ssh.close()
