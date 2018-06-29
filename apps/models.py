
from exts import db

from datetime import datetime

class BannerModel(db.Model):
    __tablename__ = 'banner'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(100), nullable=False)
    prioirty = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.now)


class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class PostModel(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))

    board = db.relationship('BoardModel', backref='posts')