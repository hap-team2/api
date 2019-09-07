from peewee import *

from .base_model import BaseModel

class Topic(BaseModel):
    name = CharField()