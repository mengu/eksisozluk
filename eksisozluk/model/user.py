from datetime import datetime
from eksisozluk.model.meta import Base
from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, DateTime

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(50))
    email = Column(Unicode(100))
    joindate = Column(DateTime)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.joindate = datetime.utcnow()
