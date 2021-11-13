from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
