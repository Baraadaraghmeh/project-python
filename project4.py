from flask import *
import sqlite3
app=Flask(__name__)


@app.route('/')
def index ():
    return render_template("index25.html");


@app.route("/add")
def add ():
    return render_template("add25.html");


@app.route("/savedetails",methods=['POST','GET'])

def saveDetails():
    msg="msg"
    if request.methods=="POST":
        try:
            name=request.form["name"]
            email=request.form["email"]
            address=request.form["address"]
            with sqlite3.connect("employee.db") as con:
                cur=con.cursor()
                cur.execute("INSERT into employee (name,email,address) values(?,?,?)",(name,email,address))
                con.commit()
                msg="employee successfully Added"
        except:
            con.rollback()
            msg="We cant add employee to the list"
        finally:
            return render_template("success25.html",msg=msg)
        con.close()


        
@app.route("/view")
def view():
    con=sqlite3.connect("emplyoee.db")
    con.row_factory=sqlite3.Row    
    cur=con.cursor()       
    cur.execute("select * from employee")
    rows=cur.fetchall()
    return render_template("view25.html",rows=rows)



app.route("/delete")
def delete():
    return render_template("delete25.html")



@app.route("/deleterecord",methods=["POST"])
def deleterecord():
    id=request.form["id"]
    with sqlite3.connect("employee.db") as con:
        try:
            cur=con.cursor()
            cur.execute("delete from employee where id =?",id)
            msg="record successfully deleted"
        except:
            "cant delete record"
        finally:
            return render_template("delete_record25.html",msg=msg)


if __name__=='__main__':
    app.run()
    