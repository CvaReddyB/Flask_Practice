from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"app": "flask app", "version": "1.0.0"}


app.run(debug=True)
