#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 26, 2017
# Flask Blog App re: LaunchCode LC-101
# Rubric: http://education.launchcode.org/web-fundamentals/assignments/build-a-blog/


from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:hello@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'super_secret_key'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))
    post_date = db.Column(db.DateTime)

    def __init__(self, title, body, post_date=None):
        self.title = title
        self.body = body
        if post_date is None:
            post_date = datetime.utcnow()
        self.post_date = post_date


@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect('/blog')


@app.route('/blog', methods=['POST', 'GET'])
def blogs():
    blog_entries = Blog.query.all()
    page_title = 'Build-a-Blog'
    main_title = 'Build-a-Blog'

    if request.method == 'GET':
        if 'id' in request.args:
            blog_id = request.args.get('id')
            blog_content = Blog.query.get(blog_id)
            return render_template('post.html', blog_content=blog_content, page_title=page_title)

    return render_template('blog.html', main_title=main_title, page_title=page_title, blog_entries=blog_entries)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        if (title == '') or (body == ''):
            flash('Oops, did you forget something...?', 'error')
        else:
            new_blog = Blog(title, body)
            db.session.add(new_blog)
            db.session.commit()
            new_blog = Blog.query.order_by('-id').first()
            new_blog_redirect = new_blog.id
            return redirect('/blog?id={0}'.format(new_blog_redirect))

    page_title = 'New Blog Entry'
    main_title = 'Add New Blog Entry'

    return render_template('newpost.html', page_title=page_title, main_title=main_title)


if __name__ == '__main__':
    app.run()
