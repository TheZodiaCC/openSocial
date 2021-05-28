from __init__ import db
import models
import datetime
import re


def create_post(title, text, user_id):
    clean = re.compile('<.*?>')

    text = re.sub(clean, '', text)
    title = re.sub(clean, '', title)

    post = models.Post(title=title, content=text, date_posted=datetime.datetime.now(), user_id=user_id)

    db.session.add(post)
    db.session.commit()


def get_posts():
    posts_struct = {}
    posts_struct_item = {}

    posts = models.Post.query.all()

    for post in posts:
        author = models.User.query.filter_by(id=post.user_id).first()

        posts_struct_item["author"] = author.username
        posts_struct_item["date_posted"] = str(post.date_posted)
        posts_struct_item["title"] = post.title
        posts_struct_item["content"] = post.content

        posts_struct[post.id] = posts_struct_item.copy()

    return posts_struct
