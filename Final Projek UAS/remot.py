import paramiko
from getpass import getpass
import sys
import time
import socket

#perlu diperhatikan bahwa setiap node memiliki username dan password yang sama
user=str(input("Login as: "))
paswd = getpass()

#disini ditambahkan ip node dengan format
#ip'[0-9]{1,4}' = "'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'"
ip1 = "192.168.56.109"
ip2 = "192.168.56.110"
ip3 = "192.168.56.111" #contoh ip mati

def node(ip,user,paswd):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(hostname= ip,username= user,password= paswd,timeout=10)
        print("ONLINE")
        indicator=1
    except (socket.gaierror, socket.timeout):
        print("NODE ", ip, " OFFLINE")
        indicator=0
        sel()

    while(indicator==1):    
        try:
            while(True):
                stdin, stdout, stderr = ssh_client.exec_command('python3 math.py \n')
                con=ssh_client.get_transport().open_session()
                con.invoke_shell()
                pilihan = " "
                while(True):
                    print("NODES IP ",ip)
                    menu = str(input("1. hitung luas dan keliling segitiga\n2. hitung luas dan keliling lingkaran\n3."
                    " hitung luas dan keliling persegi\n4. Silahkan tekan 4 untuk keluar \nSilahkan pilih menu yang anda inginkan:"))
                    print('='*100)
                    if (menu=="1"):
                        alas = str(input("masukkan panjang alas : \n"))
                        b = str(input("masukkan panjang b : \n"))
                        c = str(input("masukkan panjang c : \n"))
                        tinggi = str(input("masukkan tinggi : \n"))
                        con.send("python3 math.py \n")
                        con.send(menu+'\n')
                        con.send(alas+"\n")
                        con.send(b+"\n")
                        con.send(c+"\n")
                        con.send(tinggi+'\n')
                        time.sleep(1)
                        output = con.recv(65535)
                        print(output.decode("ascii"))
                    elif (menu=="2"):
                        r = str(input("masukkan jari-jari : \n"))
                        con.send("python3 math.py \n")
                        con.send(menu+'\n')
                        con.send(r+'\n')
                        time.sleep(1)
                        output = con.recv(65535)
                        print(output.decode("ascii"))
                        print("      ")
                    elif(menu=="3") :
                        sisi = str(input("masukkan sisi : \n"))
                        con.send("python3 math.py \n")
                        con.send(menu+'\n')
                        con.send(sisi+'\n')
                        time.sleep(1)
                        output = con.recv(65535)
                        print(output.decode("ascii"))
                    elif(menu=="4") :
                        print("program selesai")
                    else:
                        print("perintah salah, kembali ke awal")
                        node(ip,user,paswd)

                    break
                sel()
        except KeyboardInterrupt:
            print("Press Ctrl-C to terminate while statement")
            sel()

def pp(ip1,ip2,user,paswd):
    ssh_client1 = paramiko.SSHClient()
    ssh_client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client1.connect(hostname= ip1,username= user,password= paswd,timeout=10)
        print("NODE ", ip1, " ONLINE")
        indicator1=1
    except (socket.gaierror, socket.timeout):
        print("NODE ", ip1, " OFFLINE")
        indicator1=0

    ssh_client2 = paramiko.SSHClient()
    ssh_client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client2.connect(hostname= ip2,username= user,password= paswd,timeout=15)
        print("NODE ", ip2, " ONLINE")
        indicator2=1
    except (socket.gaierror, socket.timeout):
        print("NODE ", ip2, " OFFLINE")
        indicator2=0
    
    while(indicator1==1 and indicator2==1):  
        try:
            while(True):
                stdin, stdout, stderr = ssh_client1.exec_command('python3 math.py \n')
                con1=ssh_client1.get_transport().open_session()
                con1.invoke_shell()

                stdin, stdout, stderr = ssh_client2.exec_command('python3 math.py \n')
                con2=ssh_client2.get_transport().open_session()
                con2.invoke_shell()
                pilihan = " "
                while(True):
                    menu = str(input("1. hitung luas dan keliling segitiga\n2. hitung luas dan keliling lingkaran\n3."
                    " hitung luas dan keliling persegi\n4. Silahkan tekan 4 untuk keluar \nSilahkan pilih menu yang anda inginkan:"))
                    print('='*100)
                    if (menu=="1"):
                        alas = str(input("masukkan panjang alas : \n"))
                        b = str(input("masukkan panjang b : \n"))
                        c = str(input("masukkan panjang c : \n"))
                        tinggi = str(input("masukkan tinggi : \n"))
                        con1.send("python3 math.py \n")
                        con1.send(menu+'\n')
                        con1.send(alas+"\n")
                        con1.send(b+"\n")
                        con1.send(c+"\n")
                        con1.send(tinggi+'\n')
                        time.sleep(1)
                        output1 = con1.recv(65535)
                        print("NODES IP ",ip1)
                        print(output1.decode("ascii"))

                        print("----------------------")

                        con2.send("python3 math.py \n")
                        con2.send(menu+'\n')
                        con2.send(alas+"\n")
                        con2.send(b+"\n")
                        con2.send(c+"\n")
                        con2.send(tinggi+'\n')
                        time.sleep(1)
                        output2 = con2.recv(65535)
                        print("NODES IP ",ip2)
                        print(output2.decode("ascii"))
                    elif (menu=="2"):
                        r = str(input("masukkan jari-jari : \n"))
                        con1.send("python3 math.py \n")
                        con1.send(menu+'\n')
                        con1.send(r+'\n')
                        time.sleep(1)
                        output1 = con1.recv(65535)
                        print("NODES IP ",ip1)
                        print(output1.decode("ascii"))

                        print("----------------------")

                        con2.send("python3 math.py \n")
                        con2.send(menu+'\n')
                        con2.send(r+'\n')
                        time.sleep(1)
                        output2 = con2.recv(65535)
                        print("NODES IP ",ip2)
                        print(output2.decode("ascii"))

                    elif(menu=="3") :
                        sisi = str(input("masukkan sisi : \n"))
                        con1.send("python3 math.py \n")
                        con1.send(menu+'\n')
                        con1.send(sisi+'\n')
                        time.sleep(1)
                        output1 = con1.recv(65535)
                        print("NODES IP ",ip1)
                        print(output1.decode("ascii"))


                        print("----------------------")

                        con2.send("python3 math.py \n")
                        con2.send(menu+'\n')
                        con2.send(sisi+'\n')
                        time.sleep(1)
                        output2 = con2.recv(65535)
                        print("NODES IP ",ip2)
                        print(output2.decode("ascii"))
                        print("      ")
                    elif(menu=="4") :
                        print("program selesai")
                    else:
                        print("perintah salah, kembali ke awal")
                        pp(ip1,ip2,user,paswd)

                    break
                sel()
        except KeyboardInterrupt:
            print("Press Ctrl-C to terminate while statement")
            sel()   

    while(indicator1==1 and indicator2==0):  
        try:
            while(True):
                stdin, stdout, stderr = ssh_client1.exec_command('python3 math.py \n')
                con1=ssh_client1.get_transport().open_session()
                con1.invoke_shell()

                pilihan = " "
                while(True):
                    menu = str(input("1. hitung luas dan keliling segitiga\n2. hitung luas dan keliling lingkaran\n3."
                    " hitung luas dan keliling persegi\n4. Silahkan tekan 4 untuk keluar \nSilahkan pilih menu yang anda inginkan:"))
                    print('='*100)
                    if (menu=="1"):
                        alas = str(input("masukkan panjang alas : \n"))
                        b = str(input("masukkan panjang b : \n"))
                        c = str(input("masukkan panjang c : \n"))
                        tinggi = str(input("masukkan tinggi : \n"))
                        con1.send("python3 math.py \n")
                        con1.send(menu+'\n')
                        con1.send(alas+"\n")
                        con1.send(b+"\n")
                        con1.send(c+"\n")
                        con1.send(tinggi+'\n')
                        time.sleep(1)
                        output1 = con1.recv(65535)
                        print("NODES IP ",ip1)
                        print(output1.decode("ascii"))

                        print("----------------------")

                        print("NODE ", ip2, " OFFLINE")
                    elif (menu=="2"):
                        r = str(input("masukkan jari-jari : \n"))
                        con1.send("python3 math.py \n")
                        con1.send(menu+'\n')
                        con1.send(r+'\n')
                        time.sleep(1)
                        output1 = con1.recv(65535)
                        print("NODES IP ",ip1)
                        print(output1.decode("ascii"))

                        print("----------------------")

                        print("NODE ", ip2, " OFFLINE")

                    elif(menu=="3") :
                        sisi = str(input("masukkan sisi : \n"))
                        con1.send("python3 math.py \n")
                        con1.send(menu+'\n')
                        con1.send(sisi+'\n')
                        time.sleep(1)
                        output1 = con1.recv(65535)
                        print("NODES IP ",ip1)
                        print(output1.decode("ascii"))


                        print("----------------------")

                        print("NODE ", ip2, " OFFLINE")
                    elif(menu=="4") :
                        print("program selesai")
                    else:
                        print("perintah salah, kembali ke awal")
                        pp(ip1,ip2,user,paswd)

                    break
                sel()
        except KeyboardInterrupt:
            print("Press Ctrl-C to terminate while statement")
            sel()               

    while(indicator1==0 and indicator2==1):  
        try:
            while(True):
                stdin, stdout, stderr = ssh_client2.exec_command('python3 math.py \n')
                con2=ssh_client2.get_transport().open_session()
                con2.invoke_shell()

                pilihan = " "
                while(True):
                    menu = str(input("1. hitung luas dan keliling segitiga\n2. hitung luas dan keliling lingkaran\n3."
                    " hitung luas dan keliling persegi\n4. Silahkan tekan 4 untuk keluar \nSilahkan pilih menu yang anda inginkan:"))
                    print('='*100)
                    if (menu=="1"):
                        alas = str(input("masukkan panjang alas : \n"))
                        b = str(input("masukkan panjang b : \n"))
                        c = str(input("masukkan panjang c : \n"))
                        tinggi = str(input("masukkan tinggi : \n"))
                        print("NODE ", ip1, " OFFLINE")

                        print("----------------------")
                        
                        con2.send("python3 math.py \n")
                        con2.send(menu+'\n')
                        con2.send(alas+"\n")
                        con2.send(b+"\n")
                        con2.send(c+"\n")
                        con2.send(tinggi+'\n')
                        time.sleep(1)
                        output2 = con2.recv(65535)
                        print("NODES IP ",ip2)
                        print(output1.decode("ascii"))

                    elif (menu=="2"):
                        r = str(input("masukkan jari-jari : \n"))
                        print("NODE ", ip1, " OFFLINE")

                        print("----------------------")

                        con2.send("python3 math.py \n")
                        con2.send(menu+'\n')
                        con2.send(r+'\n')
                        time.sleep(1)
                        output2 = con2.recv(65535)
                        print("NODES IP ",ip2)
                        print(output2.decode("ascii"))

                    elif(menu=="3") :
                        sisi = str(input("masukkan sisi : \n"))
                        print("NODE ", ip1, " OFFLINE")

                        print("----------------------")
                        
                        con2.send("python3 math.py \n")
                        con2.send(menu+'\n')
                        con2.send(sisi+'\n')
                        time.sleep(1)
                        output2 = con2.recv(65535)
                        print("NODES IP ",ip2)
                        print(output2.decode("ascii"))

                    elif(menu=="4") :
                        print("program selesai")
                    else:
                        print("perintah salah, kembali ke awal")
                        pp(ip1,ip2,user,paswd)

                    break
                sel()
        except KeyboardInterrupt:
            print("Press Ctrl-C to terminate while statement")
            sel()               

    while(indicator1==0 and indicator2==0):
        sel()

def sel():
    #jika jumlah node bertambah maka tambahkan perintah elif contoh
    #elif pilihan == '[0-9]{1,4}' :
    #   node(ip'[0-9]{1,4}',user,paswd)
    print("----------------------\ncontoh input : 1 \nmisal ingin 2 nodes sekaligus contoh input : 1,2"
    "\n----------------------\nLIST NODES\n1. ",ip1,"\n2. ",ip2,"\n3. ",ip3,"\n----------------------")
    pilihan = input("Masukkan pilihan Nodes yang akan mengerjakan : ")
    if pilihan == "1" :
        node(ip1,user,paswd)
    elif pilihan == "2":
        node(ip2,user,paswd)
    elif pilihan =="3":
        node(ip3,user,paswd)
    elif pilihan =="1,2":
        pp(ip1,ip2,user,paswd)
    elif pilihan =="2,1":
        pp(ip2,ip1,user,paswd)
    elif pilihan =="1,3":
        pp(ip1,ip3,user,paswd)   
    elif pilihan =="3,1":
        pp(ip3,ip1,user,paswd)     
    elif pilihan =="2,3":
        pp(ip2,ip3,user,paswd)    
    elif pilihan =="3,2":
        pp(ip3,ip2,user,paswd)
    else:
        print("perintah salah, kembali ke awal")
        sel()

sel()
