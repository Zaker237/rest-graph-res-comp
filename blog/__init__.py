import os
from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_graphql import GraphQLView

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
bcrypt = Bcrypt(app)

from rest.api import create_module as api_create_module
from blog.graphql.schema import Query, Mutation

api_create_module(app)
schema = graphene.Schema(query=Query, mutation=Mutation)

# Routes
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Blog REST API server"
    })

# add an endpoint for getting images
@app.route("/img/<filename>")
def get_file(filename):
    return send_from_directory(app.config["IMAGES_PATH"], filename)