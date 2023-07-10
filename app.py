from flask import Flask, render_template, redirect, request
#import python features to create an excel workbook
from openpyxl import Workbook
#--------------------------
import sqlite3

app = Flask(__name__)
students = []
con = sqlite3.connect('Students.db', check_same_thread=False)
@app.route("/")
def index():
    con.execute("DROP TABLE IF EXISTS Students;")
    #make the table and add some data
    con.execute('''CREATE TABLE Students(id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone INTEGER, event BOOLEAN, email TEXT)''')
    #read all the data
    return render_template("index.html")

#an app route to send all data to excel
@app.route("/send_to_excel")
def send_to_excel():

    #read all data from the table, print each record and send to excel
    tableData = con.execute('SELECT * FROM Students').fetchall()
    
    #print out all names and emails
    for row in tableData:
        name = str(row[1])
        email = str(row[5])
        phone = str(row[3])
        address = str(row[2])
        event = str(row[4])
        #print("Name: " + name + " Email: " + email + "Year" + year)
    
    #make an excel document
    workBook = Workbook()
    workBook.create_sheet("Sheet")
    workSheet1 = workBook['Sheet']
    
    count = 0

    for row in tableData:
        #position is where in the workbook to put the data, A1, B1 then A2, B2, then A3, B3 & etc
        #add the first field into the excel
        position = str("A" + str(count + 1))
        name = str(row[1])
        workSheet1[position] = name
        print("the position of the first record is " + position)

        #add the next field into the excel
        position = str("B" + str(count + 1))
        email = str(row[5])
        workSheet1[position] = email

        #add the next field into the excel                
        position = str("D" + str(count + 1))
        print(position)
        phone = str(row[3])
        workSheet1[position] = phone

        #move to the next row
        #add the next field into the excel                
        position = str("E" + str(count + 1))
        print(position)
        address = str(row[2])
        workSheet1[position] = address

          #add the next field into the excel                
        position = str("F" + str(count + 1))
        print(position)
        event = str(row[4])
        workSheet1[position] = event
        #move to the next row
        count += 1
    
    #save the excel
    workBook.save('myExcel.xlsx')
    return render_template("index.html")



@app.route("/new_user")
def new_user():
    return render_template("s2.html")

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    user = {
        "name" : request.form['m_name'],
        "address" : request.form['m_address'],
        "phone" : request.form['m_phone'],
        "event" : request.form['m_event'],
        "email" : request.form['m_email'],
    }
    con.execute('''INSERT INTO Students(name, address, phone, event, email) VALUES(?,?,?,?,?)''', (user["name"], user["address"], user["phone"], user["event"], user["email"]))
    con.commit()
    return redirect ("/tableList")

#An app route to show the data on a simple html page
@app.route("/simpleList")
def slist():
    #the next line selects all data from the chess table
    StudentSelect = con.execute("SELECT * FROM Students").fetchall()

    #Send the data to be displayed on simple list.html
    return render_template("sl.html", data=StudentSelect)

@app.route("/tableList")
def tlist():
    StudentSelect = con.execute("SELECT * FROM Students").fetchall()
    return render_template("tablelist.html", StudentSelect=StudentSelect)

def setup():
     con.execute('DROP TABLE IF EXISTS Students')
     
     con.execute('''
        CREATE TABLE Students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            phone INTEGER,
            event BOOLEAN,
            email TEXT)'''
            )     
     sqlString = '''INSERT INTO Students(name, address, phone, event, email) VALUES("Bob","f", 0481843, "yes", "bob@gmail.com")'''
     con.execute(sqlString)  
     con.commit()
     return 0
app.run(debug=True)