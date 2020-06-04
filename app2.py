from flask import Flask, render_template,request,redirect
class employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.eid = 0
        self.position = ""
    def __init__(self,n,a,e,s):
        self.name = n
        self.age = a
        self.eid = e
        self.position = s
def searchEmployee(eDict, eid):
    if eid in eDict:
        return True
    return False        
def create_employee(emp_list,name,age,eid,position):
    emp = employee(name,age,eid,position)
    if searchEmployee(emp_list, eid) == False:
        emp_list[eid] = emp
        return True
    else:
        return False
def update_employee(emp_list,eid,name,age,position):
    if searchEmployee(emp_list, eid) == True:
        emp = employee(name,age,eid,position)
        emp_list[eid] = emp
    else:
        return False
    
dummy = {"e1":"Post","e2":"Post2"}
emp_dict = {}

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods = ["GET","POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        eid = request.form["eid"]
        age = request.form["age"]
        position = request.form["position"]
        if create_employee(emp_dict,name,age,eid,position) == False:
            return render_template("Error.html", val = 1)
        else:
            return redirect("/create")
    else:
        return render_template("create.html")
@app.route("/print")
def print_emp():
    return render_template("print.html", emp_lists = emp_dict)
@app.route("/update", methods = ["GET", "POST"])
def update():
    if request.method == "POST":
        name = request.form["name"]
        eid = request.form["eid"]
        age = request.form["age"]
        position = request.form["position"]
        if update_employee(emp_dict,eid,name,age,position) == False:
            return render_template("Error.html", val = 2)
        else:
            return redirect("/update")
    else:
        return render_template("update.html")
@app.route("/delete", methods = ["GET", "POST"])
def delete():
    if request.method == "POST":
        eid = request.form["eid"]
        if searchEmployee(emp_dict, eid) == True:
            del emp_dict[eid]
            return redirect("/delete")
        else:
            return render_template("Error.html", val = 3)
    else:
        return render_template("delete.html")
@app.route("/search", methods = ["GET","POST"])
def search():
    if request.method == "POST":
        eid = request.form["eid"]
        if searchEmployee(emp_dict, eid) == True:
            return render_template("search.html",emp_lists = emp_dict,val = 1, emp = eid)
        else:
            return render_template("Error.html", val = 4)
    else:
        return render_template("search.html",emp_lists = emp_dict,val = 0)





if __name__ == "__main__":
    app.run(debug = True)