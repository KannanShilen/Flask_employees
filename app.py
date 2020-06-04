from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///emp.db"
db = SQLAlchemy(app)
class emp(db.Model):
    eid = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable = False)
    age = db.Column(db.Integer,nullable = False)
    position = db.Column(db.String(30),nullable = False)

    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position
    
    def __repr__(self):
        return f"Employee name = {self.name} \n Employee Id = {self.eid} \n Age = {self.age} \n Position = {self.position}\n\n"
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods = ["GET","POST"])
def create():
    if request.method == "POST":
        return redirect("/create")
    else:
        return render_template("create.html")


if __name__ == "__main__":
    app.run(debug = True)