from flask import jsonify, Blueprint, request
import psycopg2

users_bp = Blueprint("users", __name__)

def get_connection():
    return psycopg2.connect(
        host = 'localhost',
        database = 'gabay_gov',
        user = 'jann',
        password = '@dmin098')

get_connection()


@users_bp.route('/register', methods = ['POST'])
def register():
    conn = get_connection()
    cur = conn.cursor()

    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    government_id = data.get ('government_id')
    
    cur.execute ('''INSERT INTO organization_users 
                 (first_name, last_name, email, username, password, government_id) 
                 VALUES (%s, %s, %s, %s, %s, %s)''',
                 (first_name, last_name,email,username,password,government_id))
    conn.commit()
    cur.close()
    conn.close()

    return ({"Success":"User Added Succesfully"}), 200


@users_bp.route('/login', methods = ['POST'])
def login():
    conn = get_connection()
    cur = conn.cursor()
    
    data=request.json
    username = data.get('username')
    password = data.get('password')
        
    cur.execute('''SELECT first_name, last_name, email, username, password
                FROM organization_users 
                WHERE username=%s AND password = %s;''', (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        first_name, last_name, email, username, password = user
        fullname = f'{first_name} {last_name}'
        return jsonify({"Email": email, "Name": fullname}), 200
    
    return jsonify({"Failed": "Login Failed"}), 422