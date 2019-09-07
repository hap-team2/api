from peewee import *

from .base_model import BaseModel
from .user import User
from .topic import Topic


class Subject(BaseModel):
    name = CharField()
    user = IntegerField(default=1)
    topic = IntegerField(default=1)
