from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "burrito"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jam_with_friends.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)