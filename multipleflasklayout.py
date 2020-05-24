from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indexlayout.html")

@app.route("/more")
def more():
    return render_template("morelayout.html")

if __name__== "__main__":
    app.run()
