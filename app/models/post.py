from peewee import *

from .base_model import BaseModel
from .user import User
from .subject import Subject
from .topic import Topic


class Post(BaseModel):
    content = TextField()
    title = CharField()
    question = BooleanField(default=False)
    verified = BooleanField(default=False)
    image_url = CharField(null=True)
    video_url = CharField(null=True)
    file_url = CharField(null=True)
    user = IntegerField(default=1)
    topic = IntegerField(default=1)
    subject = IntegerField(default=1)

