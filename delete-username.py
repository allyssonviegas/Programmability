# Delete username

from netmiko import ConnectHandler

routers = [
    "192.168.0.1",
    "192.168.0.2",
    "192.168.0.3"
    ]

for each in routers:
    net_connect = ConnectHandler(device_type="cisco_ios", host=each, username="ansible", password="cisco") 
    hostname = net_connect.find_prompt()
    # Check if user exists
    result = net_connect.send_command("show run | inc ccie")

    commands = ["conf term", "no username ccie", "\n"]
    
    if "ccie" in result:
        result2 = net_connect.send_multiline_timing(commands)
        print(f"ccie was deleted from {hostname[:-1]}")
        net_connect.save_config()

