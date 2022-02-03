import datetime
import re
from blog import db, app
from flask import abort, jsonify, request
from flask_restful import Resource, fields, marshal_with
from winexam.models import User
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
    @marshal_with(login_get_fields)
    def get(self):
        args = user_login_parser.parse_args()
        username = args["username"]
        password = args["password"]

        if not username or not password:
            abort(403)

        regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

        if re.fullmatch(regex, username):
            user = User.query.filter_by(email=username).first()
        else:
            user = User.query.filter_by(username=username).first()

        print("user", user)

        if not user:
            return {
                "message": "Invalid username or password, Please try again",
                "token": "",
                "refreshToken": "",
                "ok": False
            }, 403

        if not check_password_hash(user.password, password):
            return {
                "message": "Invalid email or password, Please try again",
                "token": "",
                "refreshToken": "",
                "ok": False
            }, 403

        token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "message": "You logged in successfully.",
            "token": token,
            "refreshToken": refresh_token,
            "ok": True
        }, 200

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
