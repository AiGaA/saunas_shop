import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # or 25, 465, etc.
SMTP_USERNAME = 'amasaunas@gmail.com'
SMTP_PASSWORD = 'bufjkucxrhknpzpz'

# Sender and recipient email addresses
SENDER_EMAIL = 'amasaunas@gmail.com'
RECIPIENT_EMAIL = 'dirtbikecheck@gmail.com'

# Email message content
SUBJECT = 'Test Email'
BODY = 'This is a test email sent from Python.'

# Create a MIMEText object with the email content
message = MIMEMultipart()
message['From'] = SENDER_EMAIL
message['To'] = RECIPIENT_EMAIL
message['Subject'] = SUBJECT
message.attach(MIMEText(BODY, 'plain'))

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Enable TLS encryption
        server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Authenticate with the SMTP server
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())  # Send the email
        print('Test email sent successfully!')
except Exception as e:
    print('An error occurred:', str(e))