from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "mysecret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class Users(db.model):
    id = db.column(db.integer,primary_key=True)
    name = db.column(db.string(100))
    email = db.column(db.string(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", user=user))
    else:
        return render_template("login.html")

@app.route("/<user>", methods=["GET", "POST"])
def user(user):
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash(f"Email {email} has been saved for user {user}", "success")

        if "email" in session:
            email = session["email"]
        else:
            email = ""

        return render_template("user.html", user=user, email=email)

    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]

    session.pop("user", None)
    session.pop("email", None)
    flash(f"You have been logged out! {user}", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)

