from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "viraj" and password == "12345":

            session["user"] = username
            return redirect(url_for("dashboard"))

        flash("Invalid username or password")

    return render_template("form.html")


@app.route("/dashboard")
def dashboard():

    if "user" in session:
        return f"Welcome {session['user']}"

    return redirect(url_for("login"))


@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)