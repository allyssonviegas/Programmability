# SSH to Multiple Devices from devices file
from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'ansible',
            'password': 'cisco'
        }

        net_connect = ConnectHandler(**Router)

        print ('Connecting to ' + IP)
        print('-'*85)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*85)

# Finally close the connection
net_connect.disconnect()
