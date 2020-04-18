from flask import Blueprint, render_template

hello = Blueprint("hello", __name__)


@hello.route("/")
def home():
    return render_template("welcome.html")
