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

    # Get the argument
    argument = args[0]
    action = 0

    if argument == "start" :
        action=1
    elif argument == "stop" :
        action=0
    else:
        action=3
    
    commands = ["sh ver"]

    nodes = labnodes(LAB,JWT)

    for device in devices:
        if not is_alive(LAB,device=device):
            print("Device ",device["name"],"is not alive.")
            if action != 3:
                state(device["id"], action, LAB, JWT)
                print("Device ",device["name"],"is not alive. Action",)

        else:
            print("Device ",device["name"],"is alive. No action taken")
                    
if __name__ == "__main__":
  main()