from flask import Flask,render_template_string,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "app": "flask app",
        "version": "1.0.0",
    }

@app.route("/info")
def info():
    return render_template_string('''
    <html>
    <head>Welcome To Login Page</head>
    </html>
    ''')

@app.route("/login",methods=["POST","GET"])
def login():
    message=""
    if request.method == "POST":
        data = request.form
        if data.get("Email") == 'vspreddy378@gmail.com' and data.get("password") == "admin":
            message="Sucessfully Login"
            # return render_template("welcome/welcome.html", users=["vspreddy", "valasareddy", "vspreddy378"])
        else:
            message="Login Failed"
            # return render_template("welcome/Invalid.html")
    return render_template("login/index.html",message=message)


app.run(debug=True)