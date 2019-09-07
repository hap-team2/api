from peewee import *

from base_model import BaseModel
from user import User
from topic import Topic

class Subject(BaseModel):
    name = CharField()
    user = ForeignKeyField(User, backref='subjects')
    topic = ForeignKeyField(Topic, backref='subjects')