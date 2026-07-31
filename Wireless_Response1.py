#!/usr/bin/env python3

"""
Author: ChatGPT

Purpose:
    Prompt the user for a ticket number and a customer's name,
    then generate a standard response that can be copied into
    an email or ServiceNow ticket.
"""

# Prompt the user for information
ticket_number = input("Enter the ticket number: ")
customer_name = input("Enter the customer's name: ")

print("\n" + "=" * 70)
print("Wireless Support Response")
print("=" * 70)

print(f"""
Hello {customer_name},

This email is in response to ticket number {ticket_number}.

I am sending this message to find out more information in regards to this
wireless issue.

Specifically, if you are still having connectivity, latency, or any other
wireless-related issues, please list them in your reply.

Also, please reply with the following information so that I can check the
wireless logs and coverage in your area:

• Your Name:
• Username:
• Machine Name:
• Location (Building/Floor/Cubicle, if applicable):
• Approximate time the issue occurred:
• Are you connected to Wi-Fi or using a docking station?

Once I receive this information, I will continue investigating the issue and
provide an update as soon as possible.

Thank you,

Network Support
""")

print("=" * 70)
