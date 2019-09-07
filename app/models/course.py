from peewee import *

from base_model import BaseModel

class Course(BaseModel):   
    name = CharField()