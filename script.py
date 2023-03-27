from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "app": "flask app",
        "version": "1.0.0",
    }


@app.route("/user/")
def user_list():
    return {
        "app": "flask app",
        "version": "1.0.0",
        "name": "users",
    }


app.run(debug=True)
