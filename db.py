"""
#------------------Kiasoft Internship------------------#
| Name :- Sagar Parmar                                 |
| Intern ID :- CR660                                   |
| Project Name :- CRUD APPLICATION USING DATABASE      |
#------------------------------------------------------#
"""
import sqlite3
database = "crud.db"
class DB:
    def execute_query(self,query,parameter = ()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Employee(
                emp_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                emp_name TEXT, designation TEXT, salary INT)
            """)
            res = self.cursor.execute(query,parameter)
            conn.commit()
            return res

