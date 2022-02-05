import os
import requests
import json
import random

from faker import Faker
from blog import app, db
from blog.models import User, Post, Comment, Category
from flask_bcrypt import generate_password_hash

def create_db():
    db.drop_all()
    db.session.commit()
    db.create_all()
    db.session.commit()

def create_user():
    user = User()
    user.username = os.environ.get("BLOG_USER_USERNAME")
    user.email = os.environ.get("BLOG_USER_EMAIL")
    user.name = os.environ.get("BLOG_USER_NAME")
    user.is_active = True
    password = os.environ.get("BLOG_USER_PASSWORD")
    user.password = generate_password_hash(password).decode("utf8")

    db.session.add(user)
    db.session.commit()

    return user.id

def create_categories(faker):
    cat = Category()
    cat.name = "first Category"
    cat.description = faker.sentence()
    
    cat2 = Category()
    cat2.name = "second Category"
    cat2.description = faker.sentence()
    
    cat3 = Category()
    cat3.name = "third Category"
    cat3.description = faker.sentence()

    db.session.add(cat)
    db.session.add(cat2)
    db.session.add(cat3)
    db.session.commit()

    return cat.id

def get_category():
    cats = Category.query.all()
    index = random.randint(0, len(cats)-1)
    cat = cats[index]

    return cat.id

def get_post():
    posts = Post.query.all()
    index = random.randint(0, len(posts)-1)
    post = posts[index]

    return post.id

def create_blog_posts(user_id, num_post, faker):
    for i in range(num_post):
        post = Post()
        post.title = f"Blog post number {i+1}"
        post.user_id = user_id
        post.category_id = get_category()

        post.intro = ". ".join(faker.texts(nb_texts=6))
        post.subtitle1 = faker.sentence()
        post.subtext1 = ". ".join(faker.texts(nb_texts=10))
        post.subtitle2 = faker.sentence()
        post.subtext2 = ". ".join(faker.texts(nb_texts=10))
        post.subtitle3 = faker.sentence()
        post.subtext3 = ". ".join(faker.texts(nb_texts=10))
        post.subtitle4 = faker.sentence()
        post.subtext4 = ". ".join(faker.texts(nb_texts=10))
        post.subtitle5 = faker.sentence()
        post.subtext5 = ". ".join(faker.texts(nb_texts=10))
        post.conclusion = ". ".join(faker.texts(nb_texts=10))

        db.session.add(post)
        db.session.commit()

def create_comments(user_id, num_comments, faker):
    for _ in range(num_comments):
        post_id = get_post()
        comment = Comment()
        comment.post_id = post_id
        comment.user_id = user_id
        comment.text = ". ".join(faker.texts(nb_texts=10))

        db.session.add(comment)
        db.session.commit()

def main(faker):
    create_categories(faker)
    num_post = 10000
    num_comments = 50000
    user_id = create_user()

    print("--------start post----------")
    create_blog_posts(user_id, num_post, faker)
    print("--------End post----------")
    print("--------start comments----------")
    create_comments(user_id, num_comments, faker)
    print("--------End comment----------")


if __name__ == "__main__":
    print("--------Start Creating fake data----------")
    create_db()
    faker = Faker()
    main(faker)
    print("--------End----------")