from flask import Flask 
from users import users_bp
from events import events_bp
from emails import emails_bp

app = Flask(__name__)

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(events_bp, url_prefix="/events")
app.register_blueprint(emails_bp, url_prefix="/emails")


if __name__ == '__main__':
    app.run(debug=True)