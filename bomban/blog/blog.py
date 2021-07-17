from flask import Blueprint, render_template, request, session, redirect, url_for

blog = Blueprint('blog', __name__)

@blog.route('/')
def index():
    return render_template('blog.html')
