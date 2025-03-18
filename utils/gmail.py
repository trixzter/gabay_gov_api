import os
import smtplib
import dotenv
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from dao import email_dao


def reset_password():
  dotenv.load_dotenv()
  EMAIL_ADDRESS = os.getenv('EMAIL_USER')
  EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

      subject = 'FORGET PASSWORD'
      body = 'click here to reset your password'

      msg = f'Subject: {subject}\n\n{body}'

      smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)


def event_notification():
  dotenv.load_dotenv()
  
  EMAIL_ADDRESS = os.getenv('EMAIL_USER')
  EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'EVENT NOTIFICATION'
    body = 'this is a event notification'

    msg = f'Subject: {subject}\n\n{body}'

    email_tuples = email_dao.get_emails()
    
    email_list = [email_tuple[0] for email_tuple in email_tuples]

    if email_list:
      for recipient_email in email_list:
        smtp.sendmail(EMAIL_ADDRESS, [recipient_email], msg)


def create_event_notification(title, description):
  dotenv.load_dotenv()
  
  EMAIL_ADDRESS = os.getenv('EMAIL_USER')
  EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  subject = title
  body = description
  msg = f'Subject: {subject}\n\n{body}'

  email_tuples = email_dao.get_emails()
    
  email_list = [email_tuple[0] for email_tuple in email_tuples]

  if email_list:
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
          smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
          for recipient_email in email_list:
            smtp.sendmail(EMAIL_ADDRESS, recipient_email, msg)

            
# if __name__ == '__main__':
#   # reset_password()
#   event_notification()