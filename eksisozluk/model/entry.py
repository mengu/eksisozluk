from datetime import datetime
from eksisozluk.model.meta import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, UnicodeText, DateTime

class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(50))
    user = Column(Integer, ForeignKey("user.id"))
    vote_count = Column(Integer)
    dateline = Column(DateTime)

    def __init__(self, title, user, dateline):
        self.title = title
        self.user = user
        self.dateline = datetime.utcnow()

class Entry(Base):
    __tablename__ = "entry"

    id = Column(Integer, primary_key=True)
    topic = Column(Integer, ForeignKey("topic.id"))
    user = Column(Integer, ForeignKey("user.id"))
    entry = Column(UnicodeText)
    vote_count = Column(Integer)
    dateline = Column(DateTime)

    def __init__(self, topic, user, entry):
        self.topic = topic
        self.user = user
        self.entry = entry
        self.dateline = datetime.utcnow()

class Vote(Base):
    __tablename__ = "vote"

    id = Column(Integer, primary_key=True)
    entry = Column(Integer, ForeignKey("entry.id"))
    user = Column(Integer, ForeignKey("user.id"))
    vote = Column(Integer)
    dateline = Column(DateTime)

    def __init__(self, entry, user, vote):
        self.entry = entry
        self.user = user
        self.vote = vote

        self.dateline = datetime.utcnow()
