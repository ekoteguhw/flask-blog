from flask import Flask, render_template, flash, redirect, url_for, session, logging, g
import sqlite3
from data import Posts, Post
from util import Post_format

app = Flask(__name__)

DATABASE = "flask_blog.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    posts = Posts()
    posts = Post_format(posts)
    return render_template("pages/index.html", posts=posts)

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/contact")
def contact():
    return render_template("pages/contact.html")

@app.route("/posts")
def index():
    posts = Posts()
    posts = Post_format(posts)
    return render_template("pages/posts.html", posts=posts)

@app.route("/posts/<string:id>/")
def post(id):
    post = Post(id)
    post = Post_format(post)
    return render_template("pages/post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)