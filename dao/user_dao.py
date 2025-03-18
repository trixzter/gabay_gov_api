from init_db import get_connection


def create_user(first_name:str, last_name:str, email:str, username:str, password:str, government_id:str):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('''INSERT INTO organization_users 
              (first_name, last_name, email, username, password, government_id)
              VALUES (%s, %s, %s, %s, %s, %s)''',
              (first_name, last_name, email, username, password, government_id))
  conn.commit()
  cur.close()
  conn.close()


def login_user(username:str, password:str):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('''SELECT first_name, last_name, email, username FROM organization_users 
              WHERE username = %s AND password = %s''', (username, password))
  user = cur.fetchone()
  cur.close()
  conn.close()

  return user


def update_user(id:int, first_name:str, last_name:str, email:str, username:str, password:str, government_id:str):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('''UPDATE organization_users 
                SET first_name = %s, last_name = %s, email = %s, username = %s, password = %s, government_id = %s 
                WHERE id = %s''', (first_name, last_name, email, username, password, government_id, id))
  conn.commit()
  cur.close()
  conn.close()


def check_email_dao(id:int):
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute('SELECT id FROM organization_users WHERE id = %s', (id,))
  check_email_dao = cur.fetchone() is not None
  cur.close()
  conn.close()

  return check_email_dao