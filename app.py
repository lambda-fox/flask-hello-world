# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask
# create the application object
app = Flask(__name__)
app.config["DEBUG"] = True

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!...!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

@app.route("/integer/<int:value>")
def type(value):
	print value+1
	return "Correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello {}".format(name), 200
	else:
		return "Name not found", 404

# start the development server using the run() method
if __name__ == "__main__":
    app.run()