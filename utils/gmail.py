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
      body = 'this is a forget password email'

      msg = f'Subject: {subject}\n\n{body}'

      smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)


# def event_notification():
#   dotenv.load_dotenv()
  
#   EMAIL_ADDRESS = os.getenv('EMAIL_USER')
#   EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

#   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#     subject = 'EVENT NOTIFICATION'
#     body = 'this is a new event email'

#     msg = f'Subject: {subject}\n\n{body}'

#     emails = email_dao.get_emails()
    
#     subscriber_emails = [email[0] for email in emails]

#     if subscriber_emails:
#       for receiver_email in subscriber_emails:
#         smtp.sendmail(EMAIL_ADDRESS, [receiver_email], msg)


def create_event_notification(title, description):
  dotenv.load_dotenv()
  
  EMAIL_ADDRESS = os.getenv('EMAIL_USER')
  EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

  subject = title
  body = description
  msg = f'Subject: {subject}\n\n{body}'

  emails = email_dao.get_emails()
    
  subscriber_emails = [email[0] for email in emails]

  if subscriber_emails:
      with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
          smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
          for receiver_email in subscriber_emails:
            smtp.sendmail(EMAIL_ADDRESS, receiver_email, msg)

            
# if __name__ == '__main__':
#   # reset_password()
#   event_notification()