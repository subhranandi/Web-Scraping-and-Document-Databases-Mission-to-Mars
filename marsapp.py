from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
#app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app, uri="mongodb://localhost:27017/marsdb")
#mongo = PyMongo(app)


@app.route("/")
def home():
    destination_data = mongo.db.mars.find_one()
    return render_template("index.html", mars=destination_data)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    
    #mars = mongo.db.mars
    mongo.db.mars.update({}, mars_data, upsert=True)
    #return redirect("http://localhost:5000/", code=302)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
