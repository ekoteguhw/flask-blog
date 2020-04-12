from flask import Flask, render_template
from app import app
from app.data import Posts, Post
from app.util import Post_format

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