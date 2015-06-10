from sqlalchemy.dialects.postgresql import UUID
from podhub.website import db
from . import Base


class User(Base, db.Model):
    __tablename__ = 'user'
    profile = db.relationship('Profile', backref='user', lazy='dynamic',
                              uselist=False)


class Profile(Base, db.Model):
    __tablename__ = 'profile'
    username = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    display_name = db.Column(db.String(80), index=True, unique=True)
    first_name = db.Column(db.String(80), index=True)
    last_name = db.Column(db.String(80), index=True)
    user_id = db.Column(UUID, db.ForeignKey('user.id'))
    author_id = db.Column(UUID, db.ForeignKey('author.id'))

    def __init__(self, username, email, first_name=None, last_name=None,
                 display_name=None, user_id=None, author_id=None):
        self.username = username
        self.email = email
        if not display_name:
            self.display_name = username
        else:
            self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name

        self.user_id = user_id
        self.author_id = author_id


class Author(Base, db.Model):
    __tablename__ = 'author'
    name = db.Column(db.String(80), index=True)
    profile = db.relationship('Profile', backref='author', lazy='dynamic',
                              uselist=False)

    def __init__(self, name):
        self.name = name


class Publisher(Base, db.Model):
    __tablename__ = 'publisher'
    name = db.Column(db.String(80), index=True)
    profile = db.relationship('Profile', backref='publisher', lazy='dynamic',
                              uselist=False)

    def __init__(self, name):
        self.name = name
