from .comment import Comment
from .course import Course
from .post import Post
from .subject import Subject
from .topic import Topic
from .user import User


def create_tables(sqlite_db):
    with sqlite_db:
        sqlite_db.create_tables([Comment, Course, Post, Subject, Topic, User])
