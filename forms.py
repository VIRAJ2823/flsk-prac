from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , SelectField , TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    EmailField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email
)

class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    submit = SubmitField("Register")

    email = EmailField(
    "Email",
    validators=[
        DataRequired(),
        Email()
    ]
)
    semester = SelectField(
    "Semester",
    choices=[
        ("SE","Second Year"),
        ("TE","Third Year"),
        ("BE","Final Year")
    ]
)

reason = TextAreaField(
    "Reason",
    validators=[DataRequired()]
)