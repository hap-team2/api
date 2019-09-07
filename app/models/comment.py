from peewee import *

from base_model import BaseModel
from user import User
from post import Post

class Comment(BaseModel):
    content = TextField()
    title = CharField()
    response = BooleanField(default=False)
    verified = BooleanField(default=False)
    user = ForeignKeyField(User, backref='comments')
    post = ForeignKeyField(Post, backref='comments')