# before running it 
# install flask-wtf
# email-validator 

from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash
)
from forms import SignupForm, LoginForm

app = Flask(__name__)

# initializing csrf token 
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

# signup webpage -> will get and allows to post the data
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    # if everything is validated/true then registered else show the same form 
    if form.validate_on_submit():
        # show/flash the message on the website 
        flash(f"Successfully Registered {form.username.data}!")
        return redirect(url_for("home"))
    return  render_template("signup.html", title="Sign Up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        if email == "a@b.com" and pw == "12345":
            flash("Logged in Successfully!")
            return redirect(url_for("home"))
        else:
            flash("Incorrect email or password")
    return  render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)