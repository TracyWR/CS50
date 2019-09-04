from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello Tracy!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye Sunshine!"
    return render_template("index.html", headline=headline)
