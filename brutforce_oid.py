import subprocess
import time
from datetime import datetime

# скрипт брутфорсер oid на определенном ip

snmp_ip = "31.202.74.150:8500"
# sleep(delay_time)
delay_time = 1

time.sleep(delay_time)
dt = str(datetime.now())

dt = str.replace(dt," ","")
#  функция запроса в систему с перебором всех возможных комбинаций oid
#def query_system():
    # переменная указывающая максимальное число oid опрашиваемых в кусте
    # (например 1.3.6.1.20 или 1.3.6.20.20 будут максимальными для куста 1.3.6)
max_dec_oid = 20
    # переменная указывающая глубину ухода в дерево oid (то есть 20 значений через точку)
    #max_tree_depth = 20

default_start_oid = "1.3.6.1.4.1.8888."

log_filename = "/home/smartfiber/"+dt+"_"+default_start_oid+"txt"
print(log_filename)
def query_system(oid_parts, index):
    if index == len(oid_parts):
        oid_part = ".".join(oid_parts)
        res_query=default_start_oid+oid_part
        #print(res_query)
        command = "snmpget -v 2c -c public "+snmp_ip+" "+res_query+" >>"+log_filename
        print(command)
        result = subprocess.run(command,shell=True,capture_output=True,text=True)
        time.sleep(delay_time)
        #try:
            #hostname = socket.gethostbyaddr(ip_address)
            #print(f"IP: {ip_address} - Hostname: {hostname[0]}")
        #except socket.herror:
            #print(f"IP: {ip_address} - No hostname found")
        return
    
    for i in range(max_dec_oid):
        oid_parts[index] = str(i)
        query_system(oid_parts, index + 1)

    #print("hello world" + str(dt))


oid_parts = ["20", "20", "20", "20", "20", "20", "20"]
query_system(oid_parts, 0)


#result = query_system()
exit(0
