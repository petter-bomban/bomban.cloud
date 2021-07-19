from flask import Blueprint, render_template, request, session, redirect, url_for

portfolio = Blueprint('portfolio', __name__)

@portfolio.route('/')
def index():
    return render_template('portfolio.html')
