"""
#------------------Kiasoft Internship------------------#
| Name :- Sagar Parmar                                 |
| Intern ID :- CR660                                   |
| Project Name :- CRUD APPLICATION USING DATABASE      |
#------------------------------------------------------#
"""
from os import system
import time
import db as con

db=con.DB()

def add_employee():
    emp_name=str(input("Enter Name of Employee :- "))
    designation=str(input("Enter Designation of Employee :- "))
    salary=int(input("Enter Salary of Employee :- "))
    if(len(emp_name) > 0 and len(designation) > 0 and salary > 0):
        qryinsert="INSERT INTO Employee(emp_name,designation,salary) VALUES (?,?,?)"
        parameter = (emp_name,designation,salary)
        db.execute_query(qryinsert,parameter)
        print("Employee Added Successfully")
    else:
        print("Error Try again...")

def view_employee():
    res=db.execute_query("SELECT * FROM Employee")
    print("""
        .......................................................................
        \t\t\tAll Employee
        .......................................................................
        """)
    for data in res:
        print("""
        ------------------------------------------------------
          ID\t\t\t\t :- {}
          Employee Name\t\t\t :- {}
          Employee Designation\t\t "- {}
          Employee Salary\t\t :- {}
        ------------------------------------------------------
        """.format(data[0],data[1],data[2],data[3]))

def edit_employee():
    eid = int(input("Enter ID if you edit Emplyee Record : "))
    if(eid != 0):
        emp_name=str(input("Enter Name of Employee :- "))
        designation=str(input("Enter Designation of Employee :- "))
        salary=int(input("Enter Salary of Employee :- "))
        if(len(emp_name) > 0 and len(designation) > 0 and salary > 0):
            qryedit = "UPDATE Employee SET emp_name=?,designation=?,salary=? WHERE emp_id=?"
            parameter = (emp_name,designation,salary,eid)
            db.execute_query(qryedit,parameter)
            print(f"Employee {emp_name} updated Successfully!")
    else:
        print("Wrong ID")

def delete_employee():
    eid = int(input("Enter Employe ID: "))
    if(eid != 0):
        qrydel = "DELETE FROM Employee WHERE emp_id=?"
        parameter = (eid,)
        db.execute_query(qrydel,parameter)
        print("\nEmployee record Remove Successfully")
    else:
        print("Worng ID")

def search():
    ename = str(input("Enter Name of Employee : "))
    if(len(ename) > 0):
        srchemployee = "SELECT * FROM Employee WHERE emp_name LIKE ?"
        parameter = ('%{}%'.format(ename),)
        loopdata = db.execute_query(srchemployee,parameter)
        print("""
                Search Resul is:
            """)
        for data in loopdata:
            print(""" 
        ------------------------------------------------------
          ID\t\t\t\t :- {}
          Employee Name\t\t\t :- {}
          Employee Designation\t\t :- {}
          Employee Salary\t\t :- {}
        ------------------------------------------------------
        """.format(data[0],data[1],data[2],data[3]))

while True:
    print("=========================================")
    print("\tCRUD Application")
    print("=========================================")
    print("\t[1] Add Employee Record")
    print("\t[2] View Employee Record")
    print("\t[3] Update Employee Record")
    print("\t[4] Delete Employee Record")
    print("\t[5] Search Employee Record")
    print("\t[6] Exit")
    print("=========================================")

    try:
        option = int(input("Selecciona una opcion: "))
        if(option == 1):
            add_employee()
            time.sleep(1)
            system("clear")
        elif (option == 2):
            view_employee()
            time.sleep(1)
        elif (option == 3):
            edit_employee()
            time.sleep(1)
            system("clear")
        elif (option == 4):
            delete_employee()
            time.sleep(1)
            system("clear")
        elif (option == 5):
            search()
            time.sleep(1)
            system("clear")
        elif (option == 6):
            break
    except:
        print("Something Worng, Please Try again.")
        system("clear")
