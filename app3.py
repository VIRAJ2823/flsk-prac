from flask import Flask, redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "home.html",
        name="viraj",  
        age=17,
        college="SPPU"
        )

@app.route("/users")
def users():
    return "user page "


if __name__ == "__main__":
    app.run(debug=True)