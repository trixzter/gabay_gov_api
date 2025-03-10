import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='gabay_gov',
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


def insert_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""INSERT INTO organization_users 
                (first_name, last_name, email, username, password, government_id)
                VALUES ('Chrisostomo', 'Ibarra', 'chrisostomoibarra@gmail.com', 'ibarra123', 'chris123','govid'),
                ('Maria', 'Clara', 'mariaclara@gmail.com', 'mariaclara', 'maria123', 'govid');
                """)
    
    cur.execute('''INSERT INTO subscription_emails
                (subscriber_email) VALUES ('padredamaso@gmail.com');''')
    
    cur.execute ('''INSERT INTO events
                 (title, date, time, location, photo, description)
                 VALUES ('libreng tuli', '2025-04-04', '9:00:00', 'lipa city', 'sampleimg1.jpg', 'libreng tuli para sa lahat'),
                 ('libreng pagupit', '2025-05-05', '10:00:00', 'lipa city', 'sampleimg2.jpg', 'libreng pagupit para sa lahat')
                    ''')
    
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    initialize_db()
    insert_data()