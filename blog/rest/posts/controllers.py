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
        "author": blog.user.username,
        "title": blog.title,
        "intro": blog.intro,
        "subtitle1": blog.subtitle1,
        "subtext1": blog.subtext1,
        "subtitle2": blog.subtitle2,
        "subtext2": blog.subtext2,
        "subtitle3": blog.subtitle3,
        "subtext3": blog.subtext3,
        "subtitle4": blog.subtitle4,
        "subtext4": blog.subtext4,
        "subtitle5": blog.subtitle5,
        "subtext5": blog.subtext5,
        "created_at": blog.created_at.strftime('%Y-%m-%d %H:%M:%S')
        #"comments": blog.comments
    }

class BlogApi(Resource):
    @marshal_with(blog_get_fields)
    def get(self):
        args = blog_get_parser.parse_args()

        user_id = args["user"]
        user = User.query.get(user_id)
        if not user_id:
            abort(404)

        if args["blog"]:
            blog = Post.query.get(args["blog"])
            if not blog:
                abort(404)
            
            return format_blog(blog), 200
        else:
            blogs = Post.query.all()

            return [format_blog(blog) for blog in blogs], 200


    @marshal_with(blog_post_fields)
    def post(self):
        pass

    @marshal_with(blog_put_fields)
    def put(self):
        pass

    @marshal_with(blog_delete_fields)
    def delete(self):
        pass
