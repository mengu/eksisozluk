from datetime import datetime
from eksisozluk.model.meta import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Boolean, Unicode, UnicodeText, DateTime

class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    sender = Column(Integer, ForeignKey("user.id"))
    receiver = Column(Integer, ForeignKey("user.id"))
    subject = Column(Unicode(100))
    message = Column(UnicodeText)
    folder = Column(Integer)
    read = Column(Boolean)
    dateline = Column(DateTime)

    def __init__(self, sender, receiver, subject, message):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.message = message
        self.dateline = datetime.utcnow()

