from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # rolls = db.relationship('Roll', backref='table')

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    rolls = db.relationship('Roll', backref='table')

class Roll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, server_default = db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    table_id = db.Column(db.Integer, db.ForeignKey(Table.id))
    
