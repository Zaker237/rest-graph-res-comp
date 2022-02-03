from flask_restful import fields

class MyDateFormat(fields.Raw):
    def format(self, value):
        return value.strftime('%Y-%m-%d')

comment_get_fields = {
    "id": fields.String(),
    "text": fields.String(),
    "created_at": MyDateFormat()
}

blog_get_fields = {
    "id": fields.Integer(),
    "author": fields.String(),
    "genre": fields.String(),
    "title": fields.String(),
    "intro": fields.String(),
    "subtitle1": fields.String(),
    "subtext1": fields.String(),
    "subtitle2": fields.String(),
    "subtext2": fields.String(),
    "subtitle3": fields.String(),
    "subtext3": fields.String(),
    "subtitle4": fields.String(),
    "subtext4": fields.String(),
    "subtitle5": fields.String(),
    "subtext5": fields.String(),
    "created_at": MyDateFormat(),
    "comments": fields.List(comment_get_fields)
}

blog_post_fields = {
   
}

blog_put_fields = {
    
}

blog_delete_fields = {
    
}