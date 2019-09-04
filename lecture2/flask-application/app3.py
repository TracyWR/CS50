import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = (now.month == 1 and now.day == 1)
    names= ["Alice", "Bob", "Judy"]
    return render_template("newyear.html", new_year=new_year, names = names)

@app.route("/more")
def more():
    return render_template("more.html", headline="more...")
