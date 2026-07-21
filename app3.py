from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html",
        name="Viraj Balfe",
        age=17,
        college="SPPU",
        students=["viraj", "rahul", "akanksha"]   )

@app.route("/login")
def form():
    return render_template("form.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    search_text = request.args["query"]
    return f"you have searched for :{search_text}"

if __name__ == "__main__":
    app.run(debug=True)
