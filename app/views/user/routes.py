from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_mail import Message

from app import db, mail
from app.models import User

from .forms import CreateAccountForm, LogInForm
from .utils import generate_verification_token, verify_verification_token

user = Blueprint("user", __name__)


@user.route("/")
def index():
    return render_template("user/index.html")


@user.route("/create-account", methods=["GET", "POST"])
def create_account():
    form = CreateAccountForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email_id=form.email_id.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()

        token = generate_verification_token({"email_id": form.email_id.data})

        verification_url = url_for(".verify_token", token=token, _external=True)
        full_name = f"{form.first_name.data} {form.last_name.data}"

        msg = Message("Verify your email", recipients=[form.email_id.data])
        msg.body = render_template(
            "user/emails/verify_email.txt", full_name=full_name, link=verification_url
        )
        msg.html = render_template(
            "user/emails/verify_email.html", full_name=full_name, link=verification_url
        )
        mail.send(msg)
        return redirect(url_for(".verify_account", email_id=form.email_id.data))
    return render_template("user/create_account.html", form=form)


@user.route("/verify-account")
def verify_account():
    email_id = request.args.get("email_id")
    user = User.query.filter_by(email_id=email_id).first()
    if not user:
        return redirect(url_for(".index"))
    if user.is_active:
        return redirect(url_for(".index"))

    return render_template("user/verify_account.html", email_id=email_id)


@user.route("/verify/<token>", methods=["GET", "POST"])
def verify_token(token):
    data = verify_verification_token(token)
    print(data)
    if "email_id" in data:
        user = User.query.filter_by(email_id=data["email_id"]).first()
        user.is_active = True
        db.session.commit()
        flash("Email verified successfully!", "success")
        return redirect(url_for(".index"))
    else:
        flash(data, "warning")
        return redirect(url_for(".create_account"))


@user.route("/login", methods=["GET", "POST"])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        return redirect(url_for(".index"))
    return render_template("user/sign_in.html", form=form)
