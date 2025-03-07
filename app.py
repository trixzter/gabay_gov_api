from flask import Flask 
from users import users_bp
from events import events_bp

app = Flask(__name__)

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(events_bp, url_prefix="/events")


if __name__ == '__main__':
    app.run(debug=True)