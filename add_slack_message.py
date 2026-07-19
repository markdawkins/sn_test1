# ---------------------------------------------------
# Send Report to Slack
# ---------------------------------------------------

slack_token = os.getenv("SLACK_BOT_TOKEN")

if slack_token:

    client = WebClient(token=slack_token)

    report = []
    report.append("*Cisco Interface Troubleshooting Report*")
    report.append("")
    report.append(f"*Ticket:* {ticket_number}")
    report.append(f"*Hostname:* {hostname}")
    report.append(f"*Interface:* {interface}")
    report.append("")

    for item in results:
        report.append(f"*Command:* `{item['command']}`")
        report.append("```")
        report.append(item["output"])
        report.append("```")
        report.append("")

    slack_message = "\n".join(report)

    try:

        #
        # Replace with the Slack User ID
        # Example: U04ABCD1234
        #
        USER_ID = "UXXXXXXXX"

        # Open a direct message with the user
        dm = client.conversations_open(users=USER_ID)

        channel_id = dm["channel"]["id"]

        # Send the report
        client.chat_postMessage(
            channel=channel_id,
            text=slack_message
        )

        print("\nSlack message sent successfully.")

    except SlackApiError as e:
        print(f"\nSlack Error: {e.response['error']}")

else:
    print("\nSLACK_BOT_TOKEN environment variable not set.")
