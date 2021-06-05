from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

@app.route("/<name>/<location>")
def index(name,location):
    user = User(name=name, location=location)
    db.session.add(user)
    db.session.commit()
    return "<h1> Adicionado novo usuario!</h1>"

@app.route("/<name>")
def get_user(name):
    user = User.query.filter_by(name=name).first()
    return f'<h1> O usuario se localiza em: {user.location} <h1>'
