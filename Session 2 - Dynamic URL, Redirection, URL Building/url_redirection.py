import time
from flask import Flask, redirect, url_for            

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home page!</h1>"


@app.route("/pass")
def passed():
    return "<h1>Congratz, you've passed!</h1>"


@app.route("/fail")
def failed():
    return "<h1>Sorry, you've failed!</h1>"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        time.sleep(1)
        # redirect user to page 'fail'
        return redirect(url_for("failed"))         # pass function failed to the url_for() -> to generate url for that function
    else:
        time.sleep(1)
        # redirect user to page 'pass'
        return redirect(url_for("passed"))         # pass function passed to url_for() -> to generate url for that function


if __name__ == "__main__":
    app.run(debug=True)