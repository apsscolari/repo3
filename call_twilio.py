from twilio.rest import Client

# Fake Twilio credentials (dummy for testing purposes)
account_sid = "AC1234567890abcdef1234567890abcdef"
auth_token = "1234567890abcdef1234567890abcdef"

def send_sms():
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello from Twilio!",
        from_="+12345678901",  # Dummy Twilio phone number
        to="+09876543210"  # Dummy recipient phone number
    )

    print(f"Message SID: {message.sid}")

if __name__ == "__main__":
    send_sms()
