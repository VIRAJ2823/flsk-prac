from flask import Flask, render_template, redirect, flash

from models2 import db, User

from forms2 import RegisterForm, LoginForm

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user
)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "mysecretkey"

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_user = User.query.filter_by(
            username=form.username.data
        ).first()

        if existing_user:

            flash("Username already exists!")

            return redirect("/register")

        hashed_password = generate_password_hash(
            form.password.data
        )

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful!")

        return redirect("/login")

    return render_template(
        "register.html",
        form=form
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            username=form.username.data
        ).first()

        if user and check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(user)

            flash("Login Successful!")

            return redirect("/dashboard")

        flash("Invalid Username or Password!")

    return render_template(
        "login.html",
        form=form
    )


@app.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html"
    )


@app.route("/logout")
@login_required
def logout():

    logout_user()

    flash("Logged out Successfully!")

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)