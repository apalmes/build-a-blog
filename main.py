#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 2017
# Flask Blog App re: LaunchCode LC-101
# Rubric: http://education.launchcode.org/web-fundamentals/assignments/build-a-blog/


from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'super_secret_key'


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['POST', 'GET'])
def index():
    blog_entries = Blog.query.all()
    page_title = 'Build-a-Blog'
    main_title = 'Build-a-Blog'

    if request.method == 'GET':
        # requested route format -> ./blog?id=6
        # refer to Hello Flask apps from curriculum; specifically the hour & minutes /valid-time example
        # this introduces GET requests with query parameters / data in the URL route
        # the format is: ```return redirect('/blog?id={0}'.format(id))```
        id = request.args.get('id')
        return '<html> blog post </html>...'

    return render_template("blog.html", blog_entries=blog_entries, page_title=page_title, main_title=main_title)


@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        if (title == '') or (body == ''):
            flash('You left this blank', 'error')
        else:
            new_blog = Blog(title, body)
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/')

    page_title = 'New Blog Entry'
    main_title = 'Add New Blog Entry'

    return render_template('new_post.html', page_title=page_title, main_title=main_title)


if __name__ == '__main__':
    app.run()
