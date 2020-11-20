import psutil as psu
import time
import math
import os

print("Frekuensi CPU = ", psu.cpu_freq(percpu=False))
print("Penggunaan CPU = ", psu.cpu_percent(interval=1), "%")
print("Penggunaan Hardisk = ", psu.disk_usage('/').used/1000000, "MB /", psu.disk_usage('/').total/1000000, "MB -", psu.disk_usage("/").percent, "%")
print("Penggunaan Memory = ",psu.virtual_memory().used/1000000, "MB /",psu.virtual_memory().total/1000000,"MB -", psu.virtual_memory().percent, "%")
print("Memory Tersedia = ", psu.virtual_memory().available/1000000, "MB /",psu.virtual_memory().total/1000000,"MB -", psu.virtual_memory().available * 100 / psu.virtual_memory().total, "%")
print("Jumlah thread CPU = ", psu.cpu_count(logical = True))
inet=(os.popen('ifconfig | grep inet').readlines())
eth=(os.popen('ifconfig | grep "RX packets"').readlines())
eth2=(os.popen('ifconfig | grep "TX packets"').readlines())
b=0
for i in range(3):
     print(inet[b],eth[i],eth2[i])
     b=b+2