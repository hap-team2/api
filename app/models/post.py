from peewee import *

from base_model import BaseModel
from user import User

class Post(BaseModel):
    content = TextField()
    title = CharField()
    question = BooleanField(default=False)
    verified = BooleanField(default=False)
    user = ForeignKeyField(User, backref='posts')
