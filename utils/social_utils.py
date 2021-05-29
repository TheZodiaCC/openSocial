from __init__ import db
import models
import datetime
import re


def clean_text(text):
    clean_re = re.compile('<.*?>')

    text = re.sub(clean_re, '', text)

    return text


def create_post(title, text, username):
    text = clean_text(text)
    title = clean_text(title)

    post = models.Post(title=title, content=text, date_posted=datetime.datetime.now(), author_name=username)

    db.session.add(post)
    db.session.commit()


def create_comment(text, username, post_id):
    text = clean_text(text)

    comment = models.Comment(content=text, date_posted=datetime.datetime.now(), author_name=username, post_id=post_id)

    db.session.add(comment)
    db.session.commit()


def get_post(post_id):
    post = models.Post.query.filter_by(id=post_id).first()

    return post


def get_posts():
    posts = models.Post.query.all()

    return list(reversed(posts))


def get_comments():
    pass
