from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32))
    password = db.Column(db.String(32))


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.Text)
    ingredients = db.Column(db.Text)
    instructions = db.Column(db.Text)
    username = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String(40))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
