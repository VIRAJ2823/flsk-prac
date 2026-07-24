from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)

from wtforms.validators import (
    DataRequired,
    Length,
    Email
)

from wtforms.fields import EmailField


class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[
            DataRequired()
        ]
    )

    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[
            DataRequired()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Login")