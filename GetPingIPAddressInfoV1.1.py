#!/usr/bin/env python

#This is small auto Python script file to list pings IP addresses and outputs (min/avg/max/stddev = ) 
#and X packets transmitted, 0 packets received, 100.0% packet loss whether each ping succeeded that includes the response time as well.

#Created by Tommas Huang 
#Created date: 2019-08-01

import os

hostnames = [
    '192.168.43.2',
    '192.168.43.3',
]

#You can input a list hostnames IP address to pings.

#A host name is a combination of the name of your machine and a domain name (e.g. machinename.domain.com). 
#The purpose of a host name is readability - it's much easier to remember than an IP address. 
#All hostnames resolve to IP addresses, so in many instances they are talked about like they are interchangeable.

for hostname in hostnames:
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
    response = os.system('ping -c 5 ' + hostname)
    #ping -c count 
    #Stop after sending (and receiving) count ECHO_RESPONSE packets. If this option is not specified, ping will operate until inter-rupted.  If this option is specified in conjunction with ping
    #sweeps, each sweep will consist of count packets.

    if response == 0:
        print (hostname, 'is up')
    else:
        print (hostname, 'is down')
    #Check the pings IP address response...