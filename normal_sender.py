import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email credentials and settings
sender_email = "admin@worldvision.work"
sender_password = "Privatemail12@*"
recipient_email = "martinsflirm001@gmail.com"

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Invitation for Interview"

# Add the body text
body = "Thank you for your interest, Here are the interview questions. Please complete them and return them to me at your earliest convenience, as this is an urgent position and we only need to hire a few employees for the personal assistant role."
message.attach(MIMEText(body, "plain"))

# Specify the file you want to attach
filename = "test.docx"  # Update with your file path

# Open the file in binary mode and create a MIMEBase object
try:
    with open(filename, "rb") as attachment:
        mime_base = MIMEBase("application", "octet-stream")
        mime_base.set_payload(attachment.read())

    # Encode to base64
    encoders.encode_base64(mime_base)

    # Add header to the MIMEBase object
    mime_base.add_header("Content-Disposition", f"attachment; filename= {filename}", )

    # Attach the file to the message
    message.attach(mime_base)

    # Set up the SMTP server
    try:
        with smtplib.SMTP_SSL("mail.privateemail.com", 465) as server:
            server.login(sender_email, sender_password)  # Log in to PrivateMail account
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"Error attaching the file: {e}")
