# Show interfaces up

from netmiko import ConnectHandler

net_connect = ConnectHandler(device_type="cisco_ios", host="192.168.0.2", username="ansible", password="cisco")

result = net_connect.send_command("show ip interface bri", use_textfsm=True)

for each in result:
    if each["status"] == "up":
        print(each["interface"])
