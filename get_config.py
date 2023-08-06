#!/usr/bin/env python3
from netmiko import ConnectHandler
from getpass import getpass
from devices import *
from labapi import *
import urllib3
import sys

urllib3.disable_warnings()

def main():
    
    commands = ["sh run"]

    devices=devices_update()

    for device in devices:
        print(device["name"])
        if not is_alive(LAB,device=device):
            print("Device ",device["name"],"is not alive.")
        else:
            if device["definition"]["device_type"] == "cisco_nxos" :
                try:
                    with ConnectHandler(**device["definition"]) as net_connect:
                        try: 
                            output = net_connect.send_command("sh run")
                            with open("config/" + device["name"] + ".txt", 'w') as f:
                                f.write(output)
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
                    
if __name__ == "__main__":
  main()