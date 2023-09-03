devices = [ 
        {
            "name": "L1",
            "zone": "1",
            "role": "leaf",
            "asn": "65000",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.1.1",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/1.log",
                },
        },
        {
            "name": "L2",
            "zone": "1",
            "role": "leaf",
            "asn": "65000",            
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.1.2",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/2.log",
                },
        },
        {
            "name": "L4",
            "zone": "1",
            "role": "leaf",
            "asn": "65000",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.1.4",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/4.log",
                },
        },
        {
            "name": "S21",
            "zone": "1",
            "role": "spine",
            "asn": "65000",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.2.21",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/S21.log",
                },
        },
        {
            "name": "S22",
            "zone": "1",
            "role": "spine",
            "asn": "65000",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.2.22",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/S22.log",
                },
        },
        {
            "name": "BL31",
            "zone": "1",
            "role": "bl",
            "asn": "65000",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.31",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/BL31.log",
                },
        },
        {
            "name": "BL32",
            "zone": "1",
            "role": "bl",
            "asn": "65000",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.32",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/BL32.log",
                },
        },
        {
            "name": "SRV1",
            "zone": "1",
            "role": "ce",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.1",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/SRV1.log",
                },
        },
        {
            "name": "SRV5",
            "zone": "1",
            "role": "ce",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.5",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/SRV5.log",
                },
        },    
        {
            "name": "SRV7",
            "zone": "1",
            "role": "ce",
            "definition":
                {
                    "device_type": "linux",
                    "host": "172.16.3.7",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/SRV7.log",
                },
        },
        {
            "name": "RBL33",
            "zone": "2",
            "role": "bl",
            "asn": "65002",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.33",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RBL33.log",
                },
        },
        {
            "name": "RBL34",
            "zone": "2",
            "role": "bl",
            "asn": "65002",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.34",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RBL34.log",
                },
        },
        {
            "name": "RS41",
            "zone": "2",
            "role": "spine",
            "asn": "65002",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.41",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RS41.log",
                },
        },
        {
            "name": "RS42",
            "zone": "2",
            "role": "spine",
            "asn": "65002",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.42",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RS42.log",
                },
        },
        {
            "name": "RL51",
            "zone": "2",
            "role": "leaf",
            "asn": "65002",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.51",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RL51.log",
                },
        },
        {
            "name": "RL52",
            "zone": "2",
            "role": "leaf",
            "asn": "65002",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.52",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RL52.log",
                },
        },
        {
            "name": "RSRV1",
            "zone": "2",
            "role": "ce",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.5.1",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RSRV1.log",
                },
        },
        {
            "name": "RBL35",
            "zone": "3",
            "role": "bl",
            "asn": "65001",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.35",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RBL35.log",
                },
        },   
        {
            "name": "RBL36",
            "zone": "3",
            "role": "bl",
            "asn": "65001",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.36",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RBL36.log",
                },
        },  
        {
            "name": "RS43",
            "zone": "3",
            "role": "spine",
            "asn": "65001",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.43",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RS43.log",
                },
        },  
        {
            "name": "RS44",
            "zone": "3",
            "role": "spine",
            "asn": "65001",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.44",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RS44.log",
                },
        },  
        {
            "name": "RL53",
            "zone": "3",
            "role": "leaf",
            "asn": "65001",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.53",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RL53.log",
                },
        },  
        {
            "name": "RL54",
            "zone": "3",
            "role": "leaf",
            "asn": "65001",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.3.54",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RL54.log",
                },
        },
        {
            "name": "RSRV3",
            "zone": "3",
            "role": "ce",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.5.3",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RSRV3.log",
                },
        },   
        {
            "name": "RSRV2",
            "zone": "3",
            "role": "ce",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.5.2",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/RSRV3.log",
                },
        }, 
        {
            "name": "L3Provider",
            "zone": "0",
            "role": "transit",
            "asn": "65999",
            "definition":
                {
                    "device_type": "cisco_nxos",
                    "host": "172.16.5.200",
                    "username": "cisco",
                    "password": "cisco",
                    "session_log": "log/L3Provider.log",
                },
        },          
    ]