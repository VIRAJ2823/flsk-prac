from flask import Flask, redirect,url_for,render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "hello "

@app.route("/users")
def users():
    return "user page "


if __name__ == "__main__":
    app.run(debug=True)