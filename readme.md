# Introduction

This code is an example of pexpect code for SSH interaction with a FirePOWER sensor.

The number of use case are infinite.

- from collecting device telemetry ( Checking VPN Remote Access load on every devices )
- To debugging and troubleshooting

Every an administrator can do thru SSH admin access can be done thanks to pexpect exactly the same way

**Why pexpect and Not Netmiko ?**  :  Just because netmiko doesn't support FTD devices yet.

But netmiko is perfect for interacting with a Cisco ASA or any other Legacy Cisco Networking devices. It is more easy to use than pexpect.

## What this code does ?

the **action.yml** file contains the list of FTD devices and CLI command to send to them.

This file will be read from the top to the bottom and every devices actions will be executed in the order they are defined in the file.

The idea is basic in this example.  For each device, the script sends a CLI command and display the result in the screen.

The SSH connection is executed by the **DataRetrieval()** function.   

This function SSH to the device, wait for a prompt ( >  ) and then execute the next action. Exactly how would do a human administrator.

All results are collected and stored as lines into a list. This list is return by the function.

It is up to you to do what you want with this list => Parsing, storage into a Database or text file

And you will probably imagine how to execute more complex sequences of operations, like go to expert mode, displays some debugs and depending on result you expect, then trigger some action like start traffic captures, sending alerts, modify the device configuration.

Everything is possible !


