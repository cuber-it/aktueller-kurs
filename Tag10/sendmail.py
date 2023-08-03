import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import traceback

# Bibliothek
from collections import namedtuple

Config = namedtuple('Config', ['sender', 'receivers', 'bcc_receivers', 'password', 'server', 'port'])

def send_email(subject, message, config, context, verbose=False):
    def dosend(receivers):
        # Setup the email parameters

        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = config.sender
        msg['To'] = ", ".join(receivers)

        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        server = None
        try:
            # Try to connect to the SMTP server and send the email
            server = smtplib.SMTP(config.server, config.port)
            server.starttls(context)
            server.login(config.sender, config.password)
            text = msg.as_string()
            server.sendmail(config.sender, config.receivers, text)
            if verbose: print('Email sent!')
            return True, None
        except Exception as e:
            # If an error occurred while sending the email, print it out
            if verbose: print(f"Error: {e}")
            return False, e
        finally:
            if not None:
                server.quit()

    dosend(config.receivers) # "Normale Empfänger"
    if config.bcc_receivers: # BCC nachbilden
        for name in config.bcc_receivers:
            dosend([name])

# Benutzung
def main():
    context = "SSL Kontext der angelegt werden muss"
    try:
        # Your code here...
        pass
        sys.exit(0)
    except Exception:
        # Instantiate the namedtuple
        mail_config = Config(sender='your-email@example.com',
                receivers=['your-email@example.com'],
                bcc_receivers = ["willi.watz@irgendwo.de" ],
                password='your-email-password',
                server='smtp.example.com',
                port=587)
        error = traceback.format_exc()
        # Send an email with the traceback
        send_email("Your script encountered an error", error, context, mail_config, verbose=True)
        sys.exit(1)  # Exit the script

if __name__ == "__main__":
    main()
