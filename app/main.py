from flask import Flask
from flask_restful import Api

from entities import (
    CommentResource,
    CourseResource,
    PostResource,
    SubjectResource,
    TopicResource,
    UserResource,
)

app = Flask(__name__)
api = Api(app)

api.add_resource(CommentResource, "/comment", endpoint="comment")
api.add_resource(CourseResource, "/course", endpoint="course")
api.add_resource(SubjectResource, "/subject", endpoint="subject")
api.add_resource(TopicResource, "/topic", endpoint="topic")
api.add_resource(UserResource, "/user", endpoint="user")
api.add_resource(PostResource, "/post", endpoint="post")

if __name__ == "__main__":
    app.run(debug=True)
