from flask import Flask
# Instance of Flask
app=Flask(__name__)

# Routes
@app.route("/")
@app.route("/home")
def hello():
	return "<h1>Hello Page</h1>"

@app.route("/about")
def about():
	return "<h1>About Page</h1>"


if __name__=="__main__":
	app.run(debug=True)

