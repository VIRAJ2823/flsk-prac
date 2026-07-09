from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "mysecret123"


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", user=user))

    return render_template("login.html")


@app.route("/<user>", methods=["GET", "POST"])
def user(user):
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]

    if request.method == "POST":
        email = request.form["email"]
        session["email"] = email
        flash(f"Email '{email}' has been saved for {user}.", "success")

    email = session.get("email")

    return render_template("user.html", user=user, email=email)


@app.route("/logout")
def logout():
    user = session.get("user")

    session.pop("user", None)
    session.pop("email", None)

    if user:
        flash(f"You have been logged out! Goodbye {user}.", "info")

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)