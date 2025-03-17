from init_db import get_connection
from psycopg2.extras import RealDictCursor

def create_event(title, date, time, location, photo, description):
  conn = get_connection()
  cur = conn.cursor(cursor_factory=RealDictCursor)

  cur.execute('''
                INSERT INTO events (title, date, time, location, photo, description)
              VALUES (%s, %s, %s, %s, %s, %s)''',
              (title, date, time, location, photo, description))
  conn.commit()
  cur.close()
  conn.close()


def view_all_events(title, location):
  conn = get_connection()
  cur = conn.cursor(cursor_factory=RealDictCursor)
    
  query = 'SELECT * FROM events'
  params = []
  conditions = []

  if title:
      conditions.append("title ILIKE %s")
      params.append(f"%{title}%")
    
  if location:
    conditions.append("location ILIKE %s")
    params.append(f"%{location}%")

  if conditions:
    query += ' WHERE ' + ' AND '.join(conditions)
    
  query += ';'
    
  cur.execute(query, params)
  events = cur.fetchall()
  cur.close()
  conn.close()
  return events
  


def view_event (id):
  conn = get_connection()
  cur = conn.cursor(cursor_factory=RealDictCursor)

  cur.execute('''SELECT * 
              FROM events 
              WHERE id = %s''', 
              (id,))
  event = cur.fetchone()

  cur.close()
  conn.close()
  return event


def edit_event (id, title, date, time, location, photo, description):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('''UPDATE events 
                SET title = %s, date = %s, time = %s, location = %s, photo = %s, description = %s
                WHERE id = %s''',
                (title, date, time, location, photo, description, id))
  conn.commit()
  cur.close()
  conn.close()


def remove_event(id):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute('''DELETE FROM events 
                WHERE id = %s''', 
                (id,))
  conn.commit()
  cur.close()
  conn.close()


def check_event(id):
  conn = get_connection()
  cur = conn.cursor()

  cur.execute ('''SELECT * 
               FROM events 
               WHERE id = %s''', 
               (id,))
  event = cur.fetchone()
  return event