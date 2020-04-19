from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from app.models import User


class CreateAccountForm(FlaskForm):
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email_id = StringField("Email ID", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            Length(min=8),
            EqualTo("password", "Both passwords should be match."),
        ],
    )
    submit = SubmitField("Create new account")

    def validate_email_id(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if user:
            raise ValidationError("Sorry, this Email ID is already exists.")
        self.email_id = email_id


class LogInForm(FlaskForm):
    email_id = StringField("Email ID", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log In")

    def validate_email_id(self, email_id):
        user = User.query.filter_by(email_id=email_id.data).first()
        if not user:
            raise ValidationError("Sorry, Email ID does not exists.")

        self.email_id = email_id
