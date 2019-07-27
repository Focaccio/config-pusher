#
#WHY: builder:net || automate build of study netowrk lab scenarios by config pushing
#NAME: config-pusher ||
#WHAT: py3 ||
#TYPE: sbc || sandbox code [sbc|rfc-grade-a-aaa|pxc]
#NSE: 20190427:20190427:tbd || (now:start:end)
#AGG: focaccio_greg || (https://twitter.com/3bx)
#VER: 01~aggregated~
#VER: 02~clean~scale-without-loops-just-more~
#SDS: shewkani_piyush
#
#
###_________________________________
###_________________________________
###___begin-agg___##################
###___begin-section___##############
###_________________________________
# libraries and objects
import paramiko
import netmiko
import os
#
# objects
from subprocess import call 
from netmiko import ConnectHandler
#
###.................................
###___end-section___################
#
###___begin-section___##############
###_________________________________
#string ops testing
dso_raw_testcfg = open("cfg_lab-1v0_r-1.txt","r")
dso_str_testcfg = dso_raw_testcfg.read()
print(dso_str_testcfg)
#
###.................................
###___end-section___################
#
###___begin-section___##############
###_________________________________
#data storage objects for devcie logins
dso_raw_r1 = {
    'device_type': 'cisco_ios',
    'host': '128.11.0.201',
    'username': 'lab',
    'password': 'lab',
}
dso_raw_r2 = {
    'device_type': 'cisco_ios',
    'host': '128.11.0.202',
    'username': 'lab',
    'password': 'lab',
}
#dso_raw_r3 = {
    'device_type': 'cisco_ios',
    'host': '128.11.0.203',
    'username': 'lab',
    'password': 'lab',
}
#dso_raw_r4 = {
    'device_type': 'cisco_ios',
    'host': '128.11.0.204',
    'username': 'lab',
    'password': 'lab',
}
###.................................
###___end-section___################

###___begin-section___##############
###_________________________________
#read config .txt files into dso
cfg_r1_txt=open("cfg_lab-1v0_r-1.txt","r")
cfg_r2_txt=open("cfg_lab-1v0_r-2.txt","r")

#convert dso to paste-able format
cfg_r1_commands=cfg_r1_txt.readlines()
cfg_r2_commands=cfg_r2_txt.readlines()

#show
print (cfg_r1_commands)
print (cfg_r2_commands)

#close opens
cfg_r1_txt.close()
cfg_r2_txt.close()
###.................................
###___end-section___################
#
###___begin-section___##############
###_________________________________
#make it work...r1
net_connect = ConnectHandler(**dso_raw_r1)
#
net_connect.enable()
net_connect.config_mode()
#
net_connect.send_config_set(cfg_r1_commands)
#
#
#make it work...r2
net_connect = ConnectHandler(**dso_raw_r2)
#
net_connect.enable()

net_connect.config_mode()
#
net_connect.send_config_set(cfg_r2_commands)
#
#
###.................................
###___end-section___################
#
#
#some errors but the router gets the complete config
###.................................
###.................................
###___end-agg___####################