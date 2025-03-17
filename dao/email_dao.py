from init_db import get_connection

def create_email(subscriber_email):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute ('''INSERT INTO subscription_emails 
                (subscriber_email)
                VALUES (%s)''',
                (subscriber_email,))
  conn.commit()
  cur.close()
  conn.close()
      

def check_email(subscriber_email):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('''SELECT * 
              FROM subscription_emails 
              WHERE subscriber_email = %s''',
              (subscriber_email,))
  email_exist = cur.fetchone()
  cur.close()
  conn.close()

  return email_exist