from peewee import *

from .base_model import BaseModel
from .subject import Subject
from .user import User


class Course(BaseModel):
    name = CharField()
