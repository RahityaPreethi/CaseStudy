from netmiko import ConnectHandler
import os
class Ping_test():
  def __init__(self):
# First create the device object using a dictionary
    CSR = {
      "device_type": "cisco_ios",
      "ip": "sandbox-iosxe-latest-1.cisco.com",
      "username": "developer",
      "password": "C1sco12345"
    }

    # Next establish the SSH connection
    net_connect = ConnectHandler(**CSR)

    result = os.system("ping -c 1 " + host_name)

    #and then check the response...
    if result == 0:
      print( host_name, 'is up!')
    else:
      print (host_name, 'is down!')
    net_connect.disconnect()


host_name = "sandbox-iosxe-latest-1.cisco.com"  # example
myPing_test=Ping_test()
