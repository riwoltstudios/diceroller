from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
import models
from models import *
db.init_app(app)
db.app = app
# db.drop_all()
db.create_all()

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/tables')
def get_tables():
    tables = db.session.query(Table)
    if(not tables):
        return "None"
    ret = [{'name': t.name, 'id': t.id} for t in tables]
    # ret = [dict(t.name()) for t in tables]
    return str(json.dumps(list(ret), indent=4, sort_keys=True))

@app.route('/tables/<table_name>')
def get_table(table_name):
    table = db.session.query(Table).filter(Table.name == table_name).first()
    if(not table):
        table = Table(name = table_name)
        db.session.add(table)
        db.session.commit()
    ret = [row2dict(r) for r in table.rolls]
    # ret = row2dict()
    return json.dumps(ret)

import random
@app.route('/tables/<table_name>/<username>/roll')
def roll_at_table(table_name, username):
    table = db.session.query(Table).filter(Table.name == table_name).first()
    if(not table):
        return "No table found"
    user = db.session.query(User).filter(User.username == username).first()
    if (not user):
        user = User(username = username)
        db.session.add(user)
        db.session.commit()

    roll = random.randint(1,20)
    r = Roll(value = roll, user_id = user.id, table_id = table.id)
    db.session.add(r)
    db.session.commit()
    # return f'{r.value} {r.user_id} {r.timestamp}'
    return row2dict(r)

