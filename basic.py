from flask import Flask , redirect, url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1>Welcome to the home page</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/age/<age>")
def age(age):
    return f"Your age is {age}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run()