import sqlite3
def printDB():
    try:
        result = theCursor.execute("SELECT * FROM employees")

        for row in result:
            print('id :', row[0])
            print('Fname: ', row[1])
    except sqlite3.OperationalError:
        print("Error")
    except:
        print("Unknown Error")

db_conn = sqlite3.connect('test.db')

theCursor = db_conn.cursor()
db_conn.execute(
    "DROP TABLE IF EXISTS employees")
db_conn.commit()

try:
    db_conn.execute(
        "CREATE TABLE employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Fname TEXT NOT NULL, Lname TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

    db_conn.commit()
except sqlite3.OperationalError:
    print("Error occurred")

print("Table created")

db_conn.execute("INSERT INTO employees (Fname, Lname, Age, Address, Salary, HireDate)  VALUES ('Jan', 'Ryl', 41, 'adresik', 2000, date('now'))")

db_conn.commit()

printDB()


db_conn.close()

