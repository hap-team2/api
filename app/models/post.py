from peewee import *

from base_model import BaseModel

class Post(BaseModel):
    content = TextField()
    title = CharField()
    question = BooleanField(default=False)
    verified = BooleanField(default=False)
