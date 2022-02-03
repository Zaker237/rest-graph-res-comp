from blog import db

from datetime import datetime, time, timedelta
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(120))
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    posts = db.relationship('Post', backref="user", lazy=True)

    def __init__(self, username=""):
        self.username = username

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            name=self.name,
            email=self.email
        )


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    intro = db.Column(db.Text)
    subtitle1 = db.Column(db.String(250))
    subtext1 = db.Column(db.Text)
    subtitle2 = db.Column(db.String(250))
    subtext2 = db.Column(db.Text)
    subtitle3 = db.Column(db.String(250))
    subtext3 = db.Column(db.Text)
    subtitle4 = db.Column(db.String(250))
    subtext4 = db.Column(db.Text)
    subtitle5 = db.Column(db.String(250))
    subtext5 = db.Column(db.Text)
    conclusion = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref="post", lazy=True)
    

    def to_dict(self):
        return dict(
            id=self.id,
            author=self.user.username,
            title=self.title,
            intro=self.intro,
            subtitle1=self.subtitle1,
            subtext1=self.subtext1,
            subtitle2=self.subtitle2,
            subtext2=self.subtext2,
            subtitle3=self.subtitle3,
            subtext3=self.subtext3,
            subtitle4=self.subtitle4,
            subtext4=self.subtext4,
            subtitle5=self.subtitle5,
            subtext5=self.subtext5,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S')
            comments=self.comments
        )


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def to_dict(self):
        return dict(
            id=self.id,
            text=self.text,
            created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        )