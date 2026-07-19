#!/usr/bin/env python3

"""
Author: ChatGPT
Purpose:
    Connect to a Cisco router via SSH, execute interface
    troubleshooting commands, display the results, disconnect,
    and print a formatted report.

Requirements:
    pip install netmiko
"""

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoAuthenticationException,
    NetmikoTimeoutException,
)

# ---------------------------------------------------
# Prompt User for Information
# ---------------------------------------------------

ticket_number = input("Enter Ticket Number      : ").strip()
hostname = input("Enter Hostname/IP Address : ").strip()
interface = input("Enter Interface Number    : ").strip()
username = input("Enter Username           : ").strip()
password = getpass("Enter Password           : ")

# ---------------------------------------------------
# Cisco Device Definition
# ---------------------------------------------------

device = {
    "device_type": "cisco_ios",
    "host": hostname,
    "username": username,
    "password": password,
}

# ---------------------------------------------------
# Commands
# ---------------------------------------------------

commands = [
    f"show interface {interface} | include Description|line protocol|rate|errors",
    f"show log | include {interface}",
]

results = []

# ---------------------------------------------------
# Connect to Router
# ---------------------------------------------------

try:
    print(f"\nConnecting to {hostname}...\n")

    connection = ConnectHandler(**device)

    print("Login Successful.\n")

    # Execute commands
    for command in commands:
        print("=" * 80)
        print(f"COMMAND: {command}")
        print("=" * 80)

        output = connection.send_command(command)

        print(output)
        print()

        results.append({
            "command": command,
            "output": output
        })

    # Disconnect
    connection.disconnect()

    print("\nDisconnected from router.\n")

except NetmikoAuthenticationException:
    print("ERROR: Authentication Failed.")
    quit()

except NetmikoTimeoutException:
    print("ERROR: Connection Timed Out.")
    quit()

except Exception as e:
    print(f"ERROR: {e}")
    quit()

# ---------------------------------------------------
# Final Report
# ---------------------------------------------------

print("\n")
print("=" * 80)
print("TROUBLESHOOTING REPORT")
print("=" * 80)

print(f"Ticket Number    : {ticket_number}")
print(f"Hostname         : {hostname}")
print(f"Interface Number : {interface}")
print()

for item in results:
    print("-" * 80)
    print(f"Command : {item['command']}")
    print("-" * 80)
    print(item["output"])
    print()

print("=" * 80)
print("End of Report")
print("=" * 80)
