from flask import Blueprint, jsonify, request
import psycopg2

emails_bp = Blueprint ('emails', __name__)

def get_connection():
    return psycopg2.connect(
        host = 'localhost',
        database = 'gabay_gov',
        user = 'jann',
        password = '@dmin098')

get_connection()

@emails_bp.route('/', methods=['POST'])
def add_email ():
    conn = get_connection()
    cur = conn.cursor()

    data=request.json
    subscriber_email = data.get('subscriber_email')

    cur.execute('''SELECT subscriber_email FROM subscription_emails
                WHERE subscriber_email = %s''', (subscriber_email,))
    user = cur.fetchone()

    if user is None:
        cur.execute('''INSERT INTO subscription_emails
                    (subscriber_email) VALUES (%s)''', (subscriber_email,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify ({"Success":"Email Added Successfully"}), 200

    return jsonify ({"Error":"Email Already Exist"}), 422