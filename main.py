<<<<<<< HEAD
from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:hello@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = 'JKFe3f3SF390'

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
        id = request.args.get('id')
        return redirect('/blog.html?id={0}'.format(id))

return render_template("blog.html", blog_entries=blog_entries, page_title=page_title, main_title=main_title)

@app.route('/blog', methods=['POST', 'GET'])
def blogs():
    blog_entries = Blog.query.all()
    
    
    return render_template("post.html", blog_entries=blog_entries, page_title='Build-a-Blog', main_title='Build-a-Blog')



@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        if request.form['title'] =='' or request.form['body'] == '':
            error = flash('You left this blank', 'error')
        else:
            title = request.form['title']
            body = request.form['body']
            new_blog = Blog(title, body)
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/blog')

    return render_template('newpost.html', page_title='New Blog Entry', main_title='Add New Blog Entry')

if __name__ == '__main__':
=======
from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:hello@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
app.secret_key = 'JKFe3f3SF390'

class Blog(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect('/blog')

@app.route('/blog', methods=['POST', 'GET'])
def blogs():
    blog_entries = Blog.query.all()
    
    
    return render_template("blog.html", blog_entries=blog_entries, page_title='Build-a-Blog', main_title='Build-a-Blog')



@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        if request.form['title'] =='' or request.form['body'] == '':
            error = flash('You left this blank', 'error')
        else:
            title = request.form['title']
            body = request.form['body']
            new_blog = Blog(title, body)
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/blog')

    return render_template('newpost.html', page_title='New Blog Entry', main_title='Add New Blog Entry')

if __name__ == '__main__':
>>>>>>> f2150c6b9a348dabbc4a115c14e0285cd1a93d7a
    app.run()