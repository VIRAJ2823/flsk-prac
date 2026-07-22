from flask import Flask
from models import db

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

if __name__ == "__main__":
    app.run(debug=True)