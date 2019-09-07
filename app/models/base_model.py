from peewee import *
from playhouse.shortcuts import model_to_dict


sqlite_db = SqliteDatabase("app.db", pragmas={"journal_mode": "wal"})


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    def to_json(self):
        return model_to_dict(self)

    class Meta:
        database = sqlite_db
