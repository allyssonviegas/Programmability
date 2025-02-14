#
# Test Script for reference only
#
from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

r1 = {

    "device_type": "cisco_ios",
    "host": "192.168.0.1",
    "username": "ansible",
    "password": password,
}

r2 = {

    "device_type": "cisco_ios",
    "host": "192.168.0.2",
    "username": "ansible",
    "password": password,
}

r3 = {

    "device_type": "cisco_ios",
    "host": "192.168.0.3",
    "username": "ansible",
    "password": password,
}

command = ["\n","show ip int bri","show run int lo99"]


for device in (r1, r2, r3):
    net_connect = ConnectHandler(**device)
    result = net_connect.send_multiline_timing(command)
    #Optional --> print(net_connect.find_prompt())
    print()
    print(result)
    print ("\n","================================")
    net_connect.disconnect()
