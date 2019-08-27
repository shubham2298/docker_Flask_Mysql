from typing import List, Dict
from flask import Flask ,render_template, request
import mysql.connector
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home() -> List[Dict]:
    if request.method == "POST":
         emp_id = request.form['id']
         ename = request.form['ename']
         sal = request.form['salary']
         config = {
           'user': 'root',
           'password': 'gsLab123!',
           'host': 'db',
           'port': '3306',
           'database': 'MyDB2'
            }
         #sql_insert_query = """ INSERT INTO Emp(id, ename, salary) VALUES ('1','shubham','100')"""
         connection = mysql.connector.connect(**config)
         cursor = connection.cursor()
         result=cursor.execute("INSERT INTO Emp VALUES (%s,%s,%s)",(emp_id,ename,sal))
         #results = [{name: color} for (name, color) in cursor]
         cursor.close()
         connection.commit()
         connection.close()
         return "SUCCESS"
    return render_template('index.html',msg1 = "insert successfully")

#DELEATE
@app.route('/dele', methods=['GET', 'POST'])
def dele1() -> List[Dict]:
    if request.method == "POST":
         demp_id = request.form['did']
         config = {
           'user': 'root',
           'password': 'gsLab123!',
           'host': 'db',
           'port': '3306',
           'database': 'MyDB2'
            }
         #sql_insert_query = """ INSERT INTO Emp(id, ename, salary) VALUES ('1','shubham','100')"""
         connection = mysql.connector.connect(**config)
         cursor = connection.cursor()
         sql1 = "DELETE FROM Emp WHERE id = %s"
         #result=cursor.execute("DELETE FROM Emp WHERE id = (%s)",(demp_id))
         result=cursor.execute(sql1, (demp_id,))
         #results = [{name: color} for (name, color) in cursor]
         cursor.close()
         connection.commit()
         connection.close()
         return "DEL_SUCCESS"
    return render_template('dele.html',msg2 = "insert successfully")   

#UPDATE
@app.route('/upd', methods=['GET', 'POST'])
def upda() -> List[Dict]:
    if request.method == "POST":
         uemp_id = request.form['uid']
         usal1 = request.form['usal']
         config = {
           'user': 'root',
           'password': 'gsLab123!',
           'host': 'db',
           'port': '3306',
           'database': 'MyDB2'
            }
         #sql_insert_query = """ INSERT INTO Emp(id, ename, salary) VALUES ('1','shubham','100')"""
         connection = mysql.connector.connect(**config)
         cursor = connection.cursor()
         data = (usal1, uemp_id)
         query2 = """ UPDATE Emp SET salary = %s WHERE id = %s """
         #result=cursor.execute("DELETE FROM Emp WHERE id = (%s)",(demp_id))
         result=cursor.execute(query2, data)
         #results = [{name: color} for (name, color) in cursor]
         cursor.close()
         connection.commit()
         connection.close()
         return "UPDATE_SUCCESS"
    return render_template('update.html',msg2 = "UPDATE successfully")   




    #SHOW

@app.route('/dis') 
def show() -> List[Dict]:
        config = {
           'user': 'root',
           'password': 'gsLab123!',
           'host': 'db',
           'port': '3306',
           'database': 'MyDB2'
            }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        sql2 = "SELECT * FROM Emp "
        result=cursor.execute(sql2)
        s = "<table style='border:1px solid red'>"  
        for row in cursor:  
            s = s + "<tr>"  
        for x in row:  
            s = s + "<td>" + str(x) + "</td>"  
        s = s + "</tr>"
        return "<html><body>" + s + "</body></html>"
        
        cursor.close()
        connection.commit()
        connection.close()
        #return "<html><body>" + s + "</body></html>"     
 

# @app.route('/')  
# @app.route('/dis')  
# def show1():  
#     return "<html><body>"+s+"</body></html>" 




#@app.route('/')
#def index() -> str:
    #return json.dumps({'favorite_scolors': favorite_colors()})
    #return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True)