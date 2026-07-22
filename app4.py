from flask import Flask, render_template, request, redirect, flash
from models import db, User
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "mysecretkey"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "<h1>Authentication Project</h1>"

@app.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    password = request.form["password"]

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    flash("Registration Successful!")

    return redirect("/register")   
if __name__ == "__main__":
    app.run(debug=True)