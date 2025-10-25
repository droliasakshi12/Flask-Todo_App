from flask import Flask ,render_template,request,redirect,url_for
import pymysql

app = Flask(__name__)
db = pymysql.connect(host="localhost",user="root",password="root",database="todo")
cursor = db.cursor()


@app.route("/",methods=['GET'])

def home_page():
   cursor.execute("select * from todolist order by sno desc ")
   fetch_data=cursor.fetchall()

   return render_template("index.html",todos=fetch_data)



@app.route("/add_items",methods=['POST'])
def my_todo():
     title = request.form.get("title")
     descp = request.form.get("descp")
     
     insert_items = "insert into todolist(title,descp) values(%s,%s) "

     try:
          cursor.execute(insert_items,(title,descp))
          db.commit()

     except Exception as e :
          message = f"Error{e}" 
          db.rollback()
      
     return redirect(url_for("home_page")) 



@app.route("/display_list",methods=['GET'])
def display():
     display_query="select * from todolist order by sno desc"

     try:
          cursor.execute(display_query)
          fetch_data=cursor.fetchall()
          db.commit()


     except Exception as e:
           db.rollback()

     return render_template("index.html",todos=fetch_data)



@app.route("/delete",methods=['POST'])
def delete_todo():
     sno = request.form.get("sno")
     delete_query = "delete from todolist where sno = %s"

     try:
         cursor.execute(delete_query,(sno,))
         db.commit()

     except Exception as e :
          db.rollback()
          return(f"Error{e}")
     
     
     return redirect(url_for("home_page"))


#update data

@app.route("/updating_form", methods=['POST'])
def updating_form():
    sno = request.form['sno']
    cursor.execute("SELECT * FROM todolist WHERE sno=%s", (sno,))
    todo = cursor.fetchone()
    return render_template("updating_form.html", todo=todo)



@app.route("/update",methods=['POST'])
def update_data():
     sno = request.form.get("sno")
     title = request.form.get("title")
     descp = request.form.get("descp")

     update_query="update todolist set title=%s , descp=%s where sno=%s"

     try:
          cursor.execute(update_query,(title,descp,sno))
          db.commit()

     except Exception as e :
          db.rollback()
          return f"Error{e}"
     
     return redirect(url_for("home_page"))


      



if __name__=="__main__":
      app.run(debug = True)
      