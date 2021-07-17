from blog import blog
from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)

app.register_blueprint(blog.blog, url_prefix='/blog')

@app.route("/")
def index():
    return render_template('index.html')

app.run()
