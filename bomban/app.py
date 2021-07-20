from portfolio import portfolio
from blog import blog
from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(blog.blog, url_prefix='/blog')
app.register_blueprint(portfolio.portfolio, url_prefix='/portfolio')

@app.route("/")
def index():
    return render_template('index.html')

#app.run()