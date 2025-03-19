import os
import smtplib
import dotenv
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

sys.path.append(str(Path(__file__).parent.parent))
from dao import email_dao


def reset_password():
    dotenv.load_dotenv()
    EMAIL_ADDRESS = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'FORGET PASSWORD'
        body = 'this is a forget password email'

        message = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def create_event_notification(title:str, description:str):
    dotenv.load_dotenv()
    EMAIL_ADDRESS = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

    subject = title
    body = description
    message = f'Subject: {subject}\n\n{body}'

    emails = email_dao.get_emails()
    subscriber_emails = [email[0] for email in emails]

    if subscriber_emails:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            for receiver_email in subscriber_emails:
                try:
                    smtp.sendmail(EMAIL_ADDRESS, receiver_email, message)
                    logging.info(f"Email sent to {receiver_email}")
                except Exception:
                    logging.error(f"Failed to send email to {receiver_email}")