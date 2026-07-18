from flask import Flask, redirect,url_for,render_template

app = Flask(__name__)

@app.route("/home")
def home():
    pass

@app.route("/users")
def users():
    pass    