from flask import Flask, render_template, request, redirect
from flask.globals import g
from flask.helpers import url_for
from data import cement_plants_data
import geopandas




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

@app.route("/map", methods= ['GET', 'POST'])
def map():
    df = cement_plants_data()
    group = sorted(list(set(df['Group'])))
    state = sorted(list(set(df['State'])))
    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
    return render_template("map.html", group=group,state = state, gdf = gdf)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    return render_template("contact.html")

@app.route("/checkmap",methods=['GET', 'POST'])
def checkmap():
    if request.method=="post":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname") 
        return (first_name, last_name)
    return render_template("checkmap.html")
    
if __name__ == '__main__':
    app.run(debug=True)
