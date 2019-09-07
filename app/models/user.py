from peewee import *

from base_model import BaseModel

class User(BaseModel):
    username = CharField()
    