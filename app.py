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

@app.route('/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute ('SELECT * FROM events WHERE id=%s;', (event_id,))
    event = cur.fetchone()
    cur.close()
    conn.close()

    if event is None:
            return jsonify({"error": "Event not found"}), 404
    
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
    for event in events:
        event['time'] = event['time'].strftime('%H:%M:%S')
    
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)