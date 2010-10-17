"""The application's model objects"""
from eksisozluk.model.meta import Session, Base
from eksisozluk.model.entry import Topic, Entry, Vote
from eksisozluk.model.message import Message
from eksisozluk.model.user import User

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
