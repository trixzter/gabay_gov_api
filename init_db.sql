--creation of database using postgreSQL
Psql -U postgres
@dmin098
CREATE DATABASE gabay_gov;

--python code for creating tables inside the database
import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='my_practice',
        user='jann',
        password='@dmin098'
    )

def initialize_db():
    conn = get_connection()
    cur = conn.cursor()
        
    cur.execute('''CREATE TABLE organization_users 
                        (id SERIAL PRIMARY KEY,
                        first_name VARCHAR(255) NOT NULL,
                        last_name VARCHAR (255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        username VARCHAR(255) NOT NULL,
                        password TEXT NOT NULL,
                        government_id TEXT NOT NULL); ''')
            
    cur.execute('''CREATE TABLE subscription_emails 
                        (id SERIAL PRIMARY KEY,
                        subscriber_email VARCHAR(255) UNIQUE NOT NULL);''')
            
    cur.execute('''CREATE TABLE events 
                        (id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        date DATE NOT NULL,
                        time TIME NOT NULL,
                        location VARCHAR(255) NOT NULL,
                        photo VARCHAR(255) NOT NULL,
                        description VARCHAR (255) NOT NULL);''')
            
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    initialize_db()