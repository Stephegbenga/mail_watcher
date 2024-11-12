import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from html_content import html_content
load_dotenv()

# SMTP server configuration
smtp_server = os.getenv("smtp_server")
smtp_user = os.getenv("smtp_user")
smtp_password = os.getenv("smtp_password")
sender_email = os.getenv("sender_email")

smtp_port = 465


def send_html(receiver_email):
    subject = 'Interview Invitation'

    # Set up the MIME
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Attach the HTML content
    message.attach(MIMEText(html_content, "html"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully!")
