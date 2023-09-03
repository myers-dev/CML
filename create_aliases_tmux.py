#!/usr/bin/env python3
from devices import *

def create_aliases():
    for device in devices:
        with open("create_aliases.sh", 'w') as f:
            f.write("#!/bin/sh\n")
            f.write("\n")
            for device in devices:
                f.write("alias "+device["name"]+"='sshpass -p cisco ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no cisco@" + device["definition"]["host"] + "'\n")

def create_tmux():
    for device in devices:
        with open("create_tmux.sh", 'w') as f:
            f.write("#!/bin/sh\n")
            f.write("tmux new-session -s Lab -d\n")
            count=0
            for device in devices:
                f.write("tmux new-window -t Lab:"+str(count)+" -n "+device["name"]+ " 'sshpass -p cisco ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no cisco@"+device["definition"]["host"]+ "'\n")
                count+=1

def main():
    create_aliases()
    create_tmux()

if __name__ == "__main__":
  main()