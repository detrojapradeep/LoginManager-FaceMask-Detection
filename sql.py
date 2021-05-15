import mysql.connector
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

#DB connections
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root1590',
    database = 'employee'
)
myquery = mydb.cursor()

def validateLogin(id, password):
    query = "SELECT employee_id,employee_pwd FROM employee_login WHERE employee_id = " + id + ' AND employee_pwd = "' + password + '"'
    myquery.execute(query)
    query = myquery.fetchall()
    if len(query)==0:
        return 0

    else:
        #print("Login Successful")
        return 1

def name(id):
    query = "SELECT employee_name FROM employee_login WHERE employee_id = " + id
    myquery.execute(query)
    query = myquery.fetchall()
    return str(query).strip("()[]''',")

def markattendance(id):
    if check(id) == 1:
        q = 'Insert into employee_attend values(' + id + ',now(),curdate());'
        myquery.execute(q)
        mydb.commit()
    else:
        pass

def attendance_fetch(id):
    query = "SELECT * FROM employee_attend WHERE employee_id = " + id
    myquery.execute(query)
    query = myquery.fetchall()
    return query

# def id_lister():
#     query = "SELECT emp_id FROM emp_login"
#     myquery.execute(query)
#     query = myquery.fetchall()
    
#     q = 'Insert into employee_attendance values(' + id + ',now());'
#     return query

def check(id):
    query = "SELECT * FROM employee.employee_attend where employee_id = " + id + " and date = curdate();"
    myquery.execute(query)
    query = myquery.fetchall()
    if len(query)==0:
        return 1

    else:
        return 0