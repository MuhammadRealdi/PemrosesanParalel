import paramiko
from getpass import getpass
import sys

#perlu diperhatikan bahwa setiap node memiliki username dan password yang sama
user=str(input("Login as : "))
paswd = getpass()

#disini ditambahkan ip node dengan format
#ip'[0-9]{1,4}' = "'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'"
ip1 = "192.168.56.103"
ip2 = "192.168.56.104"

def node(ip,user,paswd):
    try:
        while(True):
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname= ip,username= user,password= paswd)
            stdin, stdout, stderr = ssh_client.exec_command('python3 v1.py')
            lines = stdout.readlines()
            lines_err = stderr.readlines()

            for i in lines_err:
                print(i)
            for i in lines:
                print(i)
        ssh_client.close()
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass
        sel()

    

def sel():
    #jika jumlah node bertambah maka tambahkan perintah elif contoh
    #elif pilihan == '[0-9]{1,4}' :
    #   node(ip'[0-9]{1,4}',user,paswd)
    pilihan = input("Masukkan pilihan : ")
    if pilihan == "1" :
        node(ip1,user,paswd)
    elif pilihan == "2":
        node(ip2,user,paswd)
    else:
        print("perintah salah, kembali ke awal")
        sel()

sel()