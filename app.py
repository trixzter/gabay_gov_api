from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='gabay_gov',
        user='jann',
        password='@dmin098')

get_connection()

@app.route('/get/<int:events_id>', methods=['GET'])
def get(events_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute ('SELECT * FROM events WHERE id=%s;', (events_id,))
    event = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(event)


if __name__ == '__main__':
    app.run(debug=True)