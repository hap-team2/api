from peewee import *

from base_model import BaseModel

class Subject(BaseModel):
    name = CharField()
    content = TextField()