import datetime
import re
from blog import db, app
from flask import abort, jsonify, request
from flask_restful import Resource, fields, marshal_with
from blog.models import User, Post
from .parsers import (
    blog_get_parser,
    blog_post_parser,
    blog_put_parser,
    blog_delete_parser,
)
from .fields import (
    blog_get_fields,
    blog_post_fields,
    blog_put_fields,
    blog_delete_fields
)

def format_blog(blog):
    return {
        "id": blog.id,
        "title": blog.username
    }

class BlogApi(Resource):
    @marshal_with(blog_get_fields)
    def get(self):
        pass

    @marshal_with(blog_post_fields)
    def post(self):
        pass

    @marshal_with(blog_put_fields)
    def put(self):
        pass

    @marshal_with(blog_delete_fields)
    def delete(self):
        pass
