from sqlalchemy.dialects.postgresql import UUID
from podhub.website import db
from . import Base, Common


tags = db.Table(
    'tags',
    db.Column('tag_id', UUID, db.ForeignKey('tag.id')),
    db.Column('podcast_id', UUID, db.ForeignKey('podcast.id'))
)


class Podcast(Base):
    language = db.Column(db.Enum(*Common.languages))
    subtitle = db.Column(db.String(80))
    summary = db.Column(db.Text)
    title = db.Column(db.String(80))
    rights = db.Colum(db.Text)
    link = db.Column(db.String(2048))

    tags = db.relationship('Tag', backref=db.backref('podcasts',
                                                     lazy='dynamic'),
                           lazy='dynamic', secondary=tags)
    image = db.relationship('Image', backref='podcast', lazy='dynamic',
                            uselist=False)

    publisher_id = db.Column(UUID, db.ForeignKey('publisher.id'))
    author_id = db.Column(UUID, db.ForeignKey('author.id'))

    def __init__(self, title, link=None, publisher_id=None, author_id=None,
                 image=None, subtitle=None, summary=None, language=None,
                 rights=None):
        self.title = title
        self.subtitle = subtitle
        self.summary = summary
        self.language = language
        self.rights = rights

        self.publisher_id = publisher_id
        self.author_id = author_id
        self.image = image


class Tag(Base):
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name


class Image(Base):
    name = db.Column(db.String(80))
    href = db.Column(db.String(2048))
    podcast_id = db.Column(UUID, db.ForeignKey('podcast.id'))

    def __init__(self, href, name=None, podcast_id=None):
        self.name = name
        self.href = href
        self.podcast_id = podcast_id
