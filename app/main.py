from flask import Flask
from flask_restful import Api

from post import Post

app = Flask(__name__)
api = Api(app)

api.add_resource(Post, "/post")

if __name__ == "__main__":
    app.run(debug=True)
