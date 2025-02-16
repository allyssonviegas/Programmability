# Send commands to Multiple Devices from devices file
from netmiko import ConnectHandler

from getpass import getpass

# Test password: cisco
password = getpass()

with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'ansible',
            'password': password,
        }

        net_connect = ConnectHandler(**Router)

        commands = ["show ip int bri","sh run | inc hostname"]
        
        hostname = (net_connect.find_prompt())

        print ('Connecting to ' + hostname + ' -----> ' + IP)
        print('-'*85)
        output = net_connect.send_multiline(commands)
        print(output)
        print()
        print('-'*85)

# Finally close the connection
net_connect.disconnect()