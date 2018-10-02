import os
from threading import Thread

from flask import Flask
import sentry_sdk
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy
from sentry_sdk.integrations.flask import FlaskIntegration

import bot

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_SECRET_URL'),
    integrations=[FlaskIntegration()]
)

# Create our app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')



# Let's create a database
db = SQLAlchemy(app)

# Some basic authentication
basic_auth = BasicAuth(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    user_num = db.Column(db.Integer, unique=True, autoincrement=True)
    permissions = db.Column(db.Integer)

    def __init__(self, name, user_num, permissions=0):
        self.name = name
        self.user_num = user_num
        self.permissions = permissions

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<User {}>'.format(self.name)


# App routes
@app.route('/')
def index():
    return '<a href="/admin/">Admin</a>'


# Build database
db.create_all()

# Admin model
admin = Admin(app, name='flask-discord-bot', template_mode='bootstrap3')

# Admin views
admin.add_view(ModelView(User, db.session))

# Make a thread for our bot to run on.
t = Thread(target=bot.run)
t.start()

if __name__ == '__main__':
    app.run()
