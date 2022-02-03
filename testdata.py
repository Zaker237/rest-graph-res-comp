import os
import requests
import json
import random

from faker import Faker
from blog import app, db
from blog.models import User, Post, Comment, Category
from flask_bcrypt import generate_password_hash

faker = Faker()

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

def create_categories():
    cat = Category()
    cat.name = "first Category"
    cat.description = faker.text(max_nb_chars=500)
    
    cat2 = Category()
    cat2.name = "second Category"
    cat2.description = faker.text(max_nb_chars=500)
    
    cat3 = Category()
    cat3.name = "third Category"
    cat3.description = faker.text(max_nb_chars=500)

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

def create_blog_posts(user_id, cat_id, num_post):
    for i in num_post:
        post = Post()
        post.title = f"Blog post number {i}"
        post.user_id = user_id
        post.category_id = cat_id

        post.subtitle1 = faker.sentence()
        post.title1 = faker.text(max_nb_chars=1000)
        post.subtitle2 = faker.sentence()
        post.title2 = faker.text(max_nb_chars=1000)
        post.subtitle3 = faker.sentence()
        post.title3 = faker.text(max_nb_chars=1000)
        post.subtitle4 = faker.sentence()
        post.title4 = faker.text(max_nb_chars=1000)
        post.subtitle5 = faker.sentence()
        post.title5 = faker.text(max_nb_chars=1000)

        db.session.add(post)
        db.session.commit()

def create_comments(user_id, num_comments):
    for _ in num_comments:
        post_id = get_post()
        comment = Comment()
        comment.post_id = post_id
        comment.user_id = user_id
        comment.text = faker.text(max_nb_chars=600)

        db.session.add(comment)
        db.session.commit()

def main():
    create_categories()
    num_post = 10000
    num_comments = 50000
    cat_id = create_cat()
    user_id = create_user()
    cat_id = get_category()

    create_blog_posts(user_id, cat_id, num_post)
    create_comments(user_id, num_comments)


if __name__ == "__main__":
    print("--------Start Creating fake data______")
    create_db()
    main()
    print("--------End______")