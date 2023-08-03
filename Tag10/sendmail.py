import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import traceback

from collections import namedtuple

# Define the namedtuple
Config = namedtuple('Config', ['sender', 'receivers', 'password', 'server', 'port'])

# Instantiate the namedtuple
mail_config = Config(sender='your-email@example.com',
                receivers=['your-email@example.com'],
                password='your-email-password',
                server='smtp.example.com',
                port=587)

def send_email(subject, message, config):
    # Setup the email parameters

    # Construct the email
    msg = MIMEMultipart()
    msg['From'] = config.sender
    msg['To'] = ", ".join(config.receivers)
    msg['Subject'] = subject
    msg.attach(MIMEText(message))

    try:
        # Try to connect to the SMTP server and send the email
        server = smtplib.SMTP(config.serve, config.port)
        server.starttls()
        server.login(config.sender, config.password)
        text = msg.as_string()
        server.sendmail(config.sender, config.receivers, text)
        server.quit()
        print('Email sent!')
    except Exception as e:
        # If an error occurred while sending the email, print it out
        print(f"Error: {e}")

def main():
    try:
        # Your code here...
        pass
    except Exception:
        error = traceback.format_exc()
        # Send an email with the traceback
        send_email("Your script encountered an error", error, mail_config)
        sys.exit(1)  # Exit the script

if __name__ == "__main__":
    main()
