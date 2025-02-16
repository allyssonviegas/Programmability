## Show ip interface brief
Multiple commands exemple
<br />

```py
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
    hostname = (net_connect.find_prompt())
    print()
    print("=========    " + hostname + "    =========   " + "\n" + result)
    print ()
    net_connect.disconnect()
```
<br />

Output from the above execution

<br />

```
=========    RT1#    =========   

RT1#show ip int bri
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.0.1     YES NVRAM  up                    up      
GigabitEthernet2       10.0.0.1        YES manual up                    up      
GigabitEthernet3       unassigned      YES NVRAM  administratively down down    
GigabitEthernet4       unassigned      YES NVRAM  administratively down down    
Loopback0              1.1.1.1         YES manual up                    up      
Loopback99             99.0.0.1        YES manual up                    up      
RT1#show run int lo99
Building configuration...

Current configuration : 63 bytes
!
interface Loopback99
 ip address 99.0.0.1 255.255.255.0
end

RT1#


=========    RT2#    =========   

RT2#show ip int bri
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.0.2     YES manual up                    up      
GigabitEthernet2       10.0.0.2        YES manual up                    up      
GigabitEthernet3       unassigned      YES unset  administratively down down    
GigabitEthernet4       unassigned      YES unset  administratively down down    
Loopback0              2.2.2.2         YES manual up                    up      
Loopback99             99.0.0.2        YES manual up                    up      
RT2#show run int lo99
Building configuration...

Current configuration : 63 bytes
!
interface Loopback99
 ip address 99.0.0.2 255.255.255.0
end

RT2#


=========    RT3#    =========   

RT3#show ip int bri
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.0.3     YES manual up                    up      
GigabitEthernet2       10.0.0.3        YES manual up                    up      
GigabitEthernet3       unassigned      YES unset  administratively down down    
GigabitEthernet4       unassigned      YES unset  administratively down down    
Loopback0              3.3.3.3         YES manual up                    up      
Loopback99             99.0.0.3        YES manual up                    up      
RT3#show run int lo99
Building configuration...

Current configuration : 63 bytes
!
interface Loopback99
 ip address 99.0.0.3 255.255.255.0
end

RT3#
```
