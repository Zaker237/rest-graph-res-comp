from flask_restful import Api
from .posts.controllers import BlogApi, BlogtexteApi, BlogTitleApi

rest_api = Api()

def create_module(app, **kwargs):
    rest_api.add_resource(
        BlogApi,
        "/rest/blog"
    )

    rest_api.add_resource(
        BlogTitleApi,
        "/rest/blog-title"
    )

    rest_api.add_resource(
        BlogtexteApi,
        "/rest/blog-text"
    )

    rest_api.init_app(app)