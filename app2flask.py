from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Bullshi!"
    return render_template("index2.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Arlo!"
    return render_template("index2.html", headline= headline)

if __name__=="__main__":
 app.run()
