import os
import requests
import json
import random

from blog import app, db
from blog.models import User, Post, Comment
from flask_bcrypt import generate_password_hash

API_ENDPOINT = "https://quizapi.io/api/v1/questions"

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

def create_cat():
    cat = Category()
    cat.name = "Computer Science"
    cat.description = "This Category should contend Survey related to Computer Science"

    db.session.add(cat)
    db.session.commit()

    return cat.id

def create_blog_posts(topic, user_id, cat_id, avatar_id):
    survey = Survey()
    survey.title = topic + "'s Survey"
    survey.description = f"This a a Survey about {topic}. it contents 10 questions."
    survey.category_id = cat_id
    survey.user_id = user_id
    survey.avatar_id = avatar_id

    db.session.add(survey)
    db.session.commit()

    return survey.id

def create_avatars():
    avatar1 = Avatar()
    avatar1.name = "avatar 1"
    avatar1.link = os.environ.get("API_BASE_ENDPOINT") + "img/q1.png"
    db.session.add(avatar1)

    avatar2 = Avatar()
    avatar2.name = "avatar 2"
    avatar2.link = os.environ.get("API_BASE_ENDPOINT") + "img/q2.png"
    db.session.add(avatar2)

    avatar3 = Avatar()
    avatar3.name = "avatar 3"
    avatar3.link = os.environ.get("API_BASE_ENDPOINT") + "img/q3.png"
    db.session.add(avatar3)

    db.session.commit()

def get_avatar():
    avatars = Avatar.query.all()
    index = random.randint(0, len(avatars)-1)
    avatar = avatars[index]

    return avatar.id


def main():
    cat_id = create_cat()
    user_id = create_user()
    

    for topic in TOPICS:
        avatar_id = get_avatar()
        survey_id = create_survey(topic, user_id, cat_id, avatar_id)
        questions = fetch_10_questions(API_ENDPOINT, topic, api_key)

        for quest in questions:
            question = Question()
            question.text = quest["question"]
            question.is_multi = False if quest["multiple_correct_answers"] == "false" else True
            question.survey_id = survey_id
            question.user_id = user_id

            db.session.add(question)
            db.session.commit()
            
            answers = list(quest["answers"].values())
            true_answers = list(quest["correct_answers"].values())

            for i in range(len(answers)):
                if answers[i]:
                    choice = Choice()
                    choice.text = answers[i]
                    choice.is_answer = True if true_answers[i] == "true" else False
                    choice.question_id = question.id
                    choice.user_id = user_id

                    db.session.add(choice)
                    db.session.commit()


if __name__ == "__main__":
    print("--------Start Creating fake data______")
    create_db()
    main()
    print("--------End______")