from flask import Flask, render_template, request, redirect
from flask.helpers import url_for


app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
@app.route("/login" ,methods = ['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials! Please Try Again'
        else:
            return redirect(url_for('map'))
    return render_template("login.html", error=error)

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
    app.run(debug=True)
