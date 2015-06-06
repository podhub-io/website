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
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email
