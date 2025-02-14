# Show system uptime

from netmiko import ConnectHandler
import threading

routers = ["192.168.0.1","192.168.0.2","192.168.0.3"]

threads =[]

def mytask(ip):
    net_connect = ConnectHandler(device_type="cisco_ios", host=ip, username="ansible", password="cisco")
    result = net_connect.send_command("show ver | inc uptime")
    print(result)


for each in routers:
    t = threading.Thread(target=mytask, args=(each,))
    threads.append(t)

for thread in threads:
    thread.start()

