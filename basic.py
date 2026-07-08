from flask import Flask

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

if __name__ == "__main__":
    app.run()