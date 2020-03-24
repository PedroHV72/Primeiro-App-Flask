from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/club")
def club():
    return render_template("club.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/blog/<newsId>")
def blogDetails(newsId):
    return render_template("blog-details.html")