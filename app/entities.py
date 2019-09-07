"""
restfull entities
"""
from flask import request
from flask_restful import Resource

from models.base_model import BaseModel
from models.comment import Comment
from models.course import Course
from models.post import Post
from models.subject import Subject
from models.topic import Topic
from models.user import User


def resource_factory(model: BaseModel) -> Resource:
    """
    resource_factory is a class factory that returns a Flask RESTful resource
    based on a peewee model.
    """

    class BaseResource(Resource):
        """
        BaseResource defines a common API for a
        JSON REST Representation of a peewee model
        """
        # pylint: disable=protected-access
        def __init__(self):
            self.__name__ = model._meta.name

        def get(self):
            """
            get will select a model's object
            """
            resources = list(model.select())
            resources = [object_.to_json() for object_ in resources]
            return resources

        def head(self):
            """
            head lists the models fields
            """
            return model._meta.sorted_field_names

        def post(self):
            data = request.json if request.json else {}

            if "user" in model._meta.sorted_field_names and "user" not in data:
                data["user"] = 2
            resource = model(**data)
            resource.save()
            return resource.to_json()

    return BaseResource


# pylint: disable=invalid-name
CommentResource = resource_factory(Comment)
CourseResource = resource_factory(Course)
PostResource = resource_factory(Post)
SubjectResource = resource_factory(Subject)
TopicResource = resource_factory(Topic)
UserResource = resource_factory(User)
