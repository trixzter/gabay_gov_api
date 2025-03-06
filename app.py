from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='gabay_gov',
        user='jann',
        password='@dmin098')

get_connection()


@app.route('/events', methods=['POST'])
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

    return ({"success":"Event Deleted Succesfully"}), 200


@app.route('/events/<int:event_id>', methods=['GET'])
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


@app.route('/events', methods=['GET'])
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


@app.route('/events/<int:event_id>', methods=['PUT'])
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

    return ({"success":"Event Updated Succesfully"}), 200


@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute ('SELECT id FROM events WHERE id = %s;', (event_id,))
    event = cur.fetchone()

    if event is None:
        cur.close()
        conn.close()
        return ({"error":"Event not found"}), 404
    
    cur.execute('DELETE FROM events WHERE id=%s;',(event_id,))
    conn.commit()
    cur.close()
    conn.close()
    return ({"success":"Event deleted succesfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)