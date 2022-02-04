import datetime
import re
from blog import db, app
from flask import abort, jsonify, request
from flask_restful import Resource, fields, marshal_with
from sqlalchemy.orm import load_only
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
    blog_delete_fields,
    blog_text_get_fields,
    blog_title_get_fields
)

def format_comment(comment):
    return {
        "id": comment.id,
        "text": coment.text,
        "created_at": comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }

def format_blog(blog):
    return {
        "id": blog.id,
        "author": blog.user.username,
        "genre": blog.category.name,
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
        "comments": list(map(format_comment, blog.comments))
    }

def format_blog_title(blog):
    return {
        "id": blog.id,
        "title": blog.title,
        "intro": blog.intro,
        "subtext1": blog.subtext1,
        "subtext2": blog.subtext2,
        "subtitle3": blog.subtitle3,
        "subtitle4": blog.subtitle4,
        "subtitle5": blog.subtitle5,
    }

def format_blog_text(blog):
    return {
        "subtext1": blog.subtext1,
        "subtext2": blog.subtext2,
        "subtext3": blog.subtext3,
        "subtext4": blog.subtext4,
        "subtext5": blog.subtext5,
        "conclusion": blog.conclusion,
    }

class BlogApi(Resource):
    @marshal_with(blog_get_fields)
    def get(self):
        args = blog_get_parser.parse_args()
        with_comments = args["comments"]

        if args["blog"]:
            blog = Post.query.get(args["blog"])
            if not blog:
                abort(404)
            
            if with_comments:
                return format_blog(blog), 200
            else:
                return blog.to_dict(), 200
        else:
            blogs = Post.query.all()

            if with_comments:
                return [format_blog(blog) for blog in blogs], 200
            else:
                return [blog.to_dict() for blog in blogs], 200

class BlogTitleApi(Resource):
    @marshal_with(blog_title_get_fields)
    def get(self):
        args = blog_get_parser.parse_args()

        fields = ["id", "title", "intro", "subtitle1", "subtitle2", "subtitle3", "subtitle4", "subtitle5"]
        blogs = db.session.query(Post).options(load_only(*fields)).all()

        return [format_blog_title(blog) for blog in blogs], 200

class BlogtexteApi(Resource):
    @marshal_with(blog_text_get_fields)
    def get(self):
        args = blog_get_parser.parse_args()

        fields = ["id", "subtext1", "subtext2", "subtext3", "subtext4", "subtext5", "conclusion"]
        blogs = db.session.query(Post).options(load_only(*fields)).all()

        return [format_blog_text(blog) for blog in blogs], 200
