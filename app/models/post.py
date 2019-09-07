from peewee import *

from base_model import BaseModel
from user import User
from comment import Comment
from subject import Subject
from topic import Topic

class Post(BaseModel):
    content = TextField()
    title = CharField()
    id_ = IntegerField()
    question = BooleanField(default=False)
    verified = BooleanField(default=False)
    image_url = CharField()
    video_url = CharField()
    file_url = CharField()
    user = ForeignKeyField(User, backref='posts')
    comment = ForeignKeyField(Comment, backref='posts')
    topic = ForeignKeyField(Topic, backref='posts', null=True)
    subject = ForeignKeyField(Subject, backref='posts')

