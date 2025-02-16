# Show clock

from netmiko import ConnectHandler

routers = ["192.168.0.1","192.168.0.2","192.168.0.3"]

for each in routers:
    net_connect = ConnectHandler(device_type="cisco_ios", host=each, username="ansible", password="cisco")
    hostname = net_connect.find_prompt()
    result = net_connect.send_command("show clock")
    print(hostname + "--->" + result)
    
