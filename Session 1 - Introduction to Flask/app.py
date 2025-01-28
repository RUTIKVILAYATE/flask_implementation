
from flask import Flask

# create the flask app
app = Flask(__name__)               # __name__ -> special variable -> that python assigns to each module (app.py file) ->

# home page
@app.route("/")     # endpoint -> whernever one reach it it will redirect to a functon which will return -> return statement
@app.route("/home")
def home():
	return "<h1>Welcome to the Home Page!</h1>"


# about page
@app.route("/about")
def about():
	return "<h1>Welcome to the About Page!</h1>"


# example of path parameter
@app.route("/welcome/<name>")              # expect a path parameter -> and by given by the user -> return the output of function below it
def welcome(name):
	return f"<h1>Hi {name.title()}, you're welcome to this Page!</h1>"


# example of integer path parameter
@app.route("/addition/<int:num>")            # expecting an integer parameter bcoz we will add them with another int then 
def addition(num):
	return f"<h1>Input is {num}, Output is {num + 10}</h1>"


# example of two integer path parameters
@app.route("/addition_two/<int:num1>/<int:num2>")       # can give two parameters with / in between them 
def addition_two(num1, num2):
	return f"<h1>{num1} + {num2} is {num1 + num2}</h1>"


# start the app
# run if and onlu if run app.py module -> means any other module cannot run flask app -> only app.py module can run it by importing it -> within itself 
if __name__ == "__main__":
	app.run(debug=True)

# therefore, for safety if we dont want any other module to start our flask app we do if __name__ == "__main__"...