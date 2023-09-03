#!/usr/bin/env python3
from netmiko import ConnectHandler
from getpass import getpass
from devices import *
from labapi import *
import urllib3
import sys

urllib3.disable_warnings()

def main():
    # Get the command line arguments
    args = sys.argv[1:]

    # Check if the user provided any arguments
    if len(args) == 0:
        print("Please provide an argument.")
        sys.exit(1)

    delay = 0
    commands=[]

    for arg in args:
        if arg == '-d':
            delay = 1
        else:
            commands.append(arg)

    devices=devices_update()

    for device in devices:
        print(device["name"],device["zone"])
        if not is_alive(LAB,device=device):
            print("Device ",device["name"],"is not alive.")
        else:
            if device["definition"]["device_type"] == "cisco_nxos" :
                try:
                    with ConnectHandler(**device["definition"]) as net_connect:
                        try: 
                            for command in commands:
                                output = net_connect.send_command(command)
                                print(command)
                                print(output)
                                print("-------------------------")
                                if delay == 1:
                                    input()
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
                    
if __name__ == "__main__":
  main()