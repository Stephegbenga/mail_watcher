import imaplib, os
import email
from email.header import decode_header
from email.utils import parseaddr
from dotenv import load_dotenv
load_dotenv()

# PrivateMail login credentials

smtp_user = os.getenv("smtp_user")
smtp_password = os.getenv("smtp_password")

# print(smtp_user)
# print(smtp_password)


def wait_for_new_messages():
    mail = imaplib.IMAP4_SSL("imap.privateemail.com")
    mail.login(smtp_user, smtp_password)

    mail.select("inbox")

    # Search for unread emails
    status, messages = mail.search(None, 'UNSEEN')
    emails = messages[0].split()

    new_emails = []

    # Process each unread email
    for mail_id in emails:
        status, msg_data = mail.fetch(mail_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                # Parse the email content
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")

                from_ = msg.get("From")
                sender_name, sender_email = parseaddr(from_)

                print("sender_email ", sender_email)
                print("Subject:", subject)

                if subject == "Job Position Interest":
                    new_emails.append(sender_email)

    mail.logout()
    return new_emails
