from flask_restful import Api
from .posts.controllers import BlogApi

rest_api = Api()

def create_module(app, **kwargs):
    rest_api.add_resource(
        BlogApi,
        "/blog"
    )

    rest_api.init_app(app)