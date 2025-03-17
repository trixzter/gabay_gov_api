from init_db import get_connection

def create_email(subscriber_email):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('''SELECT * 
              FROM subscription_emails 
              WHERE subscriber_email = %s''',
              (subscriber_email,))
  user = cur.fetchone()

  if user is None:
    cur.execute ('''INSERT INTO subscription_emails 
                (subscriber_email)
                VALUES (%s)''',
                (subscriber_email,))
    conn.commit()
    cur.close()
    conn.close()
    return True
      
  cur.close()
  conn.close()
  return None

