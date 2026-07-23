from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):

    username = StringField()

    password = PasswordField()

    submit = SubmitField()

username = StringField(
    "Username",
    validators=[DataRequired()]
)


password = PasswordField(
    "Password",
    validators=[DataRequired(), Length(min=8)]
)

