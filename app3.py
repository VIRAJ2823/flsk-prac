from flask import Flask, render_template ,request ,redirect,url_for

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html",
        name="Viraj Balfe",
        age=17,
        college="SPPU",
        students=["viraj", "rahul", "akanksha"]   )


@app.route("/login")
def login_page():
    return render_template("form.html")



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "viraj" and password == "12345":

            return redirect(url_for("dashboard"))
        
        return "invalid username or password"

        
    

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return"<h1>welcome viraj</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():
    search_text = request.args["query"]
    return f"you have searched for :{search_text}"

if __name__ == "__main__":
    app.run(debug=True)
