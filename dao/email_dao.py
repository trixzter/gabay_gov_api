from init_db import get_connection


def create_email(subscriber_email:str):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('INSERT INTO subscription_emails (subscriber_email) VALUES (%s)', (subscriber_email,))
  conn.commit()
  cur.close()
  conn.close()


def email_existing(subscriber_email:str):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('SELECT 1 FROM subscription_emails WHERE subscriber_email = %s',(subscriber_email,))
  email_exist = cur.fetchone() is not None 
  cur.close()
  conn.close()

  return email_exist


def get_emails():
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('SELECT subscriber_email FROM subscription_emails')
  emails = cur.fetchall()
  cur.close()
  conn.close()
  
  return emails