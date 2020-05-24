from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world"

@app.route("/david")
def david():
    return "Hello, david!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!!!</h1>"


if __name__=="__main__":
 app.run()