import graphene

from blog import db, app
from flask import abort
from blog.models import User, Post, Comment, Category
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

class CategoryObject(SQLAlchemyObjectType):
    class Meta:
        model = Category
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    posts = graphene.List(
        PostObject,
        blog=graphene.Int()
    )

    @staticmethod
    def resolve_posts(parent, info, blog=None):

        if blog:
            data = Post.query.get(blog)
        else:
            data = Post.query.all()

        return data


# class Mutation(graphene.ObjectType):
#     pass