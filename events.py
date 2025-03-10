from flask import jsonify, Blueprint, request
import psycopg2
from psycopg2.extras import RealDictCursor

events_bp = Blueprint ("events", __name__)

def get_connection():
    return psycopg2.connect(
        host = 'localhost',
        database = 'gabay_gov',
        user = 'jann',
        password = '@dmin098')

get_connection()


@events_bp.route('/', methods=['POST'])
def add_event():
    data = request.json 
    title = data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute ('''INSERT INTO events (title, date, time, location, photo, description) 
                VALUES (%s, %s, %s, %s, %s, %s)''',(title, date, time, location, photo, description))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"success":"Event Deleted Succesfully"}), 200


@events_bp.route('/', methods=['GET'])
def all_events():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute ('SELECT * FROM events;')
    events = cur.fetchall()
    cur.close()
    conn.close()
    
    if not events:
        return jsonify({"Error": "No events found"}), 404

    for event in events:
        event['time'] = event['time'].strftime('%H:%M:%S')
    
    return jsonify(events)


@events_bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute ('SELECT * FROM events WHERE id=%s;', (event_id,))
    event = cur.fetchone()
    cur.close()
    conn.close()

    if event is None:
        return jsonify({"Error": "Event not found"}), 404
    
    event['time'] = event['time'].strftime('%H:%M:%S')
    return jsonify(event)


@events_bp.route('/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    title=data.get('title')
    date = data.get('date')
    time = data.get('time')
    location = data.get('location')
    photo = data.get('photo')
    description = data.get('description')

    conn = get_connection()
    cur = conn.cursor()
    cur.execute('UPDATE events SET title = %s, date = %s, time = %s, location = %s, photo = %s, description = %s WHERE id=%s', 
                (title, date, time, location, photo, description, event_id))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"success":"Event Updated Succesfully"}), 200


@events_bp.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute ('SELECT id FROM events WHERE id = %s;', (event_id,))
    event = cur.fetchone()

    if event is None:
        cur.close()
        conn.close()
        return jsonify({"error":"Event not found"}), 404
    
    cur.execute('DELETE FROM events WHERE id=%s;',(event_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"success":"Event deleted succesfully"}), 200