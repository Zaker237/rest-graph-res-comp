import graphene

import blog.graphql.schemas.blog_schemas as blog_schemas


class Query(blog_schemas.Query, graphene.ObjectType):
    pass

# class Mutation(blog_schemas.Mutation, graphene.ObjectType):
#     pass
