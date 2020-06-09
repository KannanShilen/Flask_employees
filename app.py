from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5433/flask"
db = SQLAlchemy(app)
class emp(db.Model):
    eid = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30),nullable = False)
    age = db.Column(db.Integer,nullable = False)
    position = db.Column(db.String(30),nullable = False)

    def __init__(self,eid,name,age,position):
        self.eid = eid
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
        name = request.form['name']
        eid = request.form["eid"]
        position = request.form["position"]
        age = request.form["age"]
        if emp.query.get(eid) != None:
            return render_template("Error.html", val = 1)
        else:
            db.session.add(emp(eid,name,age,position))
            db.session.commit()
            return redirect("/create")
    else:
        return render_template("create.html")

@app.route("/delete", methods = ["GET","POST"])
def delete():
    if request.method == "POST":
        eid = request.form["eid"]
        if emp.query.get(eid) == None:
            return render_template("Error.html", val = 3)
        else:
            db.session.delete(emp.query.get(eid))
            db.session.commit()
            return redirect("/delete")
    else:
        return render_template("delete.html")

@app.route("/update", methods = ["GET","POST"])
def update():
    if request.method == "POST":
        eid = request.form["eid"]
        empl = emp.query.get(eid)
        if empl == None:
            return render_template("Error.html",val = 2)
        else:
            empl.name = request.form["name"]
            empl.age = request.form["age"]
            empl.position = request.form["position"]
            db.session.commit()
            return redirect("/update")
    else:
        return render_template("update.html")

@app.route("/search",methods = ["GET", "POST"])
def search():
    if request.method == "POST":
        eid = request.form["eid"]
        empl = emp.query.get(eid)
        if empl == None:
            return render_template("Error.html",val = 4)
        else:
            return render_template("search.html", val = 1, emp_lists = empl)
    else:
        return render_template("search.html", val = 0)

    



@app.route("/print")
def printemp():
    return render_template("print.html",emp = emp.query.all())



if __name__ == "__main__":
    app.run(debug = True)