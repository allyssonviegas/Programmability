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

        hostname = net_connect.send_command('show run | i host')
        hostname.split(" ")
        hostname,device = hostname.split(" ")
        print ("Backing up " + device)

        filename = '/home/user/Programmability/Python/backups/' + device + '.txt'
        # filename = device + '.txt' 

        showrun = net_connect.send_command('show run')
        showver = net_connect.send_command('show ver')
        log_file = open(filename, "a")   # in append mode
        log_file.write(showrun)
        log_file.write("\n")
        log_file.write(showver)
        log_file.write("\n")

# Finally close the connection
net_connect.disconnect()


