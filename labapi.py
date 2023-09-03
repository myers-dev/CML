import requests
import urllib3
from netmiko import ConnectHandler
from devices import *

urllib3.disable_warnings()

JWT="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb20uY2lzY28udmlybCIsImlhdCI6MTY5MjgyNDczMCwiZXhwIjoxNjkyOTExMTMwLCJzdWIiOiIwMDAwMDAwMC0wMDAwLTQwMDAtYTAwMC0wMDAwMDAwMDAwMDAifQ.AOm744DQEFhuVU0UXIRbPi1uG0JpMBDQWqk66BMwyjc"
LAB="680b8876-7e38-41e2-a259-9f4093f9c5a0"


def labnodes(labid,jwt):

    url = "https://192.168.68.94/api/v0/labs/"+labid+"/nodes?data=true"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+JWT,  
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code != 200:
        print(response.status_code)
        print(response.content)
        return ([])
    nodes = response.json()

    return nodes

def devices_update():
    nodes = labnodes(LAB, JWT)

    for node in nodes:
        for device in devices:
            if node["label"]==device["name"]:
                device["id"] = node["id"]
                break
    return devices

def state(node, state, labid, JWT):
    if state == 0:
        #stop
        url = "https://192.168.68.94/api/v0/labs/"+labid+"/nodes/"+node+"/state/stop"
    else:
        #start
        url = "https://192.168.68.94/api/v0/labs/"+labid+"/nodes/"+node+"/state/start"
    
    headers = {
     "accept": "application/json",
     "Authorization": "Bearer "+JWT,  
    }

    response = requests.put(url, headers=headers, verify=False)

    if response.status_code == 204:
        if state == 0:
            print("Node stopped successfully")
        else:
            print("Node started successfully")
    else:
        print(response.status_code)


def is_alive(labid, device):
    """ return true/false """

    url = "https://192.168.68.94/api/v0/labs/"+labid+"/nodes?data=true"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+JWT,  
    }

    response = requests.get(url, headers=headers, verify=False)

    if device["definition"]["device_type"] == "cisco_nxos":
        command="sh ver"
    elif device["definition"]["device_type"] == "linux":
        command="echo"
    else:
        print("Unhandled type",device["definition"]["device_type"])
        return False  
    try:
        with ConnectHandler(**device["definition"]) as net_connect:
            try: 
                net_connect.send_command(command)
            except Exception as e:
                return False
        return True
    except Exception as e:
        return False

    