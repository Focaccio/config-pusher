#
#WHY: builder:net || automate build of study netowrk lab scenarios by config pushing
#NAME: config-pusher ||
#WHAT: py3 ||
#TYPE: sbc || sandbox code [sbc|rfc-grade-a-aaa|pxc]
#NSE: 20190427:20190427:tbd || (now:start:end)
#AGG: greg-focaccio || (https://twitter.com/3bx)
#
#
#
# libraries
import paramiko
import netmiko
import os
#
# objects
from subprocess import call 
from netmiko import ConnectHandler
#
#string ops
dso_raw_testcfg = open("test_cfg1.txt","r")
dso_str_testcfg = dso_raw_testcfg.read()
print(dso_str_testcfg)
#
#data storage objects
dso_raw_r1 = {
    'device_type': 'cisco_ios',
    'host': '128.11.0.201',
    'username': 'lab',
    'password': 'lab',
}
#
#functions?
net_connect = ConnectHandler(**dso_raw_r1)
#
net_connect.enable()
net_connect.config_mode()
#
#read config .txt file into f
f=open("test_cfg1.txt","r")
#
#make it work...
config_commands=f.readlines()
net_connect.send_config_set(config_commands)
#
#some errors but the router gets the complete config
