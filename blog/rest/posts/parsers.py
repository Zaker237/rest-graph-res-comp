from flask_restful import reqparse

blog_get_parser = reqparse.RequestParser()
blog_get_parser.add_argument(
    "blog",
    type=int,
    location=["args", "values", "form", "json", "headers"]
)
blog_get_parser.add_argument(
    "comments",
    type=bool,
    location=["args", "values", "form", "json", "headers"]
)

blog_post_parser = reqparse.RequestParser()
blog_post_parser.add_argument(
    "id",
    type=int,
    location=["args", "values", "form", "json", "headers"]
)

blog_put_parser = reqparse.RequestParser()
blog_put_parser.add_argument(
    "id",
    type=int,
    location=["args", "values", "form", "json", "headers"],
    help="The key word of the search"
)


blog_delete_parser = reqparse.RequestParser()
blog_delete_parser.add_argument(
    "id",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)