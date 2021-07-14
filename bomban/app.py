from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', response=None, error=None, key_check=False, key=None)
