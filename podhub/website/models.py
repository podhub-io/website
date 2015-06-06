from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.func import now
import sqlalchemy
import uuid
from . import db


class Base(db.Model):
    id = db.Column(UUID, default=lambda: str(uuid.uuid4()), primary_key=True)
    created_at = db.Column(db.DateTime(), default=now())
    updated_at = db.Column(
        sqlalchemy.DateTime(), default=now(), onupdate=now())

    __mapper_args__ = {'order_by': sqlalchemy.desc('updated_at')}


class User(Base):
    profile = db.relationship('Profile', backref='user', lazy='dynamic',
                              uselist=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Profile(Base):
    username = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    display_name = db.Column(db.String(80), index=True, unique=True)
    user_id = db.Column(UUID, db.ForeignKey('user.id'))

    def __init__(self, username, email, display_name=None):
        self.username = username
        self.email = email
        if not display_name:
            self.display_name = username
        else:
            self.display_name = display_name
