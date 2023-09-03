#!/usr/bin/env python3
from netmiko import ConnectHandler
from getpass import getpass
import time
from devices import *
from labapi import *
import urllib3

urllib3.disable_warnings()

DELAY=120
START=1

started_nodes = []
devices = devices_update()

for device in devices:
    print("Starting ",device["name"])
    state(device["id"], START , LAB, JWT)
    print("Delay",DELAY," sec")
    time.sleep(DELAY)
    started_nodes.append(device)
    for started_node in started_nodes:
        print("    ",started_node["name"],"is",is_alive(LAB,started_node))

   
