from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.func import now
import sqlalchemy
import uuid
from podhub.website import db


class Base(db.Model):
    id = db.Column(UUID, default=lambda: str(uuid.uuid4()), primary_key=True)
    created_at = db.Column(db.DateTime(), default=now())
    updated_at = db.Column(
        sqlalchemy.DateTime(), default=now(), onupdate=now())

    __mapper_args__ = {'order_by': sqlalchemy.desc('updated_at')}

class Common(object):
    languages = frozenset(['en'])
