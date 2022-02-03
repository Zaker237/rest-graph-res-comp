from blog import db, app

from blog.models import User, Post, Comment, abort
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graphql_relay.node.node import from_global_id


class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)

class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)

class CommentObject(SQLAlchemyObjectType):
    class Meta:
        model = Comment
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    posts = graphene.List(
        PostObject,
        user=graphene.Int(required=True),
        blog=graphene.Int()
    )

    @staticmethod
    def resolve_posts(parent, info, user, blog=None):
        user = User.query.get(user)
        if not user:
            abort(404)

        if blog:
            data = Post.query.get(blog)
        else:
            data = Post.query.all()

        return query


class Query(graphene.ObjectType):
    pass