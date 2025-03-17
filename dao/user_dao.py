from init_db import get_connection

def register_user (first_name, last_name, email, username, password, government_id):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute ('''INSERT INTO organization_users 
              (first_name, last_name, email, username, password, government_id)
              VALUES (%s, %s, %s, %s, %s, %s)''',
              (first_name, last_name, email, username, password, government_id))
  conn.commit()
  cur.close()
  conn.close()

def login_user ( username, password):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute ('''SELECT first_name, last_name, email, username
              FROM organization_users 
              WHERE username = %s AND password = %s''', 
              (username, password))
  user = cur.fetchone()
  cur.close()
  conn.close()

  return user

def update_user (id, first_name, last_name, email, username, password, government_id):
  conn = get_connection ()
  cur = conn.cursor()

  cur.execute ('''UPDATE organization_users 
                SET first_name = %s, last_name = %s, email = %s, username = %s, password = %s, government_id = %s 
                WHERE id = %s''',
                (first_name, last_name, email, username, password, government_id, id))
  conn.commit()
  cur.close()
  conn.close()


def check_user (id):
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute('''SELECT id 
              FROM organization_users 
              WHERE id=%s''', 
              (id,))
  check_user = cur.fetchone()
  cur.close()
  conn.close()

  return check_user