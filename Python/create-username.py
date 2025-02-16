# Create Username

from netmiko import ConnectHandler

routers = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

commands = ["username ccie privilege 15 secret cisco"]

for each in routers:
    net_connect = ConnectHandler(device_type="cisco_ios", host=each, username="ansible", password="cisco")
    hostname = net_connect.find_prompt()
    net_connect.send_config_set(commands)

    result = net_connect.send_command("show run | inc ccie")
    print(hostname + "--->" + result)
