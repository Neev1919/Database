from tkinter import*
root = Tk()
import sqlite3
connection = sqlite3.connect ("myTable.db")
crsr = connection.cursor()
'''sql_command = """ CREATE TABLE emp (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR (30),
geneder CHAR(1),
joining DATE);"""
crsr.execute(sql_command)'''
'''sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M",
"2014-03-28");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M",
"2014-03-28");"""
crsr.execute(sql_command)'''
connection.commit()
connection.close()
def Submit ():
    connection = sqlite3.connect ("myTable.db")
    crsr = connection.cursor()
    crsr.execute ("INSERT INTO emp VALUES (:Staffno,  :f_name, :l_name ,:Gender , :DOJi)",
                {
                  "Staffno" : Staffno.get(),
                  "f_name" : f_name.get(),
                  "l_name" : l_name.get(),
                  "Gender" : Gender.get(),
                  "DOJi" : DOJi.get(),
                }
            )
    connection.commit()
    connection.close()
    Staffno.delete (0 ,END)
    f_name.delete (0 ,END)
    l_name.delete (0 ,END)
    Gender.delete (0 ,END)
    DOJi.delete (0 ,END)
def Query():
    connection = sqlite3.connect ("myTable.db")
    crsr = connection.cursor()
    crsr.execute ("SELECT *, oid FROM emp")
    ans = crsr.fetchall()
    records = ""
    for record in ans:
        records += str(record [0])+ " " +record [1] +" " +record[2] + " " +record [3]+ " " + record [4]+ "\n"
    Label (root , text = records).grid(row = 7, column = 0 , columnspan =2)
Staffno = Entry (root, width = 30)
Staffno.grid (row = 0 ,column = 1, padx = 20)
f_name = Entry (root, width = 30)
f_name.grid (row = 1 ,column = 1, padx = 20)
l_name = Entry (root, width = 30)
l_name.grid (row = 2 ,column = 1, padx = 20)
Gender = Entry (root, width = 30)
Gender.grid (row = 3 ,column = 1, padx = 20)
DOJi = Entry (root, width = 30)
DOJi.grid (row = 4 ,column = 1, padx = 20)

Staffno_label = Label (root, text = "Staff Number")
Staffno_label.grid (row = 0, column =0)
f_name_label = Label (root, text = "First Name")
f_name_label.grid (row = 1, column =0)    
l_name_label = Label (root, text = "Last Name")
l_name_label.grid (row = 2, column =0)
Gender_label = Label (root, text = "Gender")
Gender_label.grid (row = 3, column =0)
DOJi_label = Label (root, text = "Date of Joining")
DOJi_label.grid (row = 4, column =0)    
deli_label = Label (root , text = "Enter the ID of person to be deleted")
deli_label.grid( row = 7 , column = 0)
deli = Entry (root , width = 30)
deli.grid (row = 7 , column = 1 , padx = 20)
Button (root, text = "Add record to data base" , command = Submit).grid (row = 5 , columnspan = 2, pady = 10, padx = 20, ipadx = 100)
Button (root, text = "Query the database" , command = Query).grid (row = 6 , columnspan = 2, pady = 10, padx = 20, ipadx = 100)
def delete():
    connection = sqlite3.connect ("myTable.db")
    crsr = connection.cursor()
    connection.execute("DELETE from emp where oid =" + deli.get())
    deli.delete (0 , END)
    connection.commit()
Button (root , text = "Delete the enter ID" , command = delete).grid (row =8 , columnspan = 2 , pady=10 , padx = 20 , ipadx = 100)
def update():
    up = Tk()
    connection = sqlite3.connect ("myTable.db")
    crsr = connection.cursor()
    record_id = deli.get()
    crsr.execute ("SELECT * FROM emp WHERE staff_number = " + record_id)
    records = crsr.fetchall()
    global Staffno_edit
    Staffno_edit = Entry (up , width = 30)
    Staffno_edit.grid (row = 0 , column = 1, padx = 20)
    global f_name_edit
    f_name_edit = Entry (up , width = 30)
    f_name_edit.grid (row = 1 , column = 1, padx = 20) 
    global l_name_edit
    l_name_edit = Entry (up , width = 30)
    l_name_edit.grid (row = 2 , column = 1, padx = 20)
    global Gender_edit
    Gender_edit = Entry (up , width = 30)
    Gender_edit.grid (row = 3 , column = 1, padx = 20)  
    global DOJi_edit
    DOJi_edit = Entry (up , width = 30)
    DOJi_edit.grid (row = 4 , column = 1, padx = 20) 
    Staffno_label = Label (up, text = "Staff Number")
    Staffno_label.grid (row = 0, column =0)
    f_name_label = Label (up, text = "First Name")
    f_name_label.grid (row = 1, column =0)    
    l_name_label = Label (up, text = "Last Name")
    l_name_label.grid (row = 2, column =0)
    Gender_label = Label (up, text = "Gender")
    Gender_label.grid (row = 3, column =0)
    DOJi_label = Label (up, text = "Date of Joining")
    DOJi_label.grid (row = 4, column =0)
    for record in records:
        Staffno_edit.insert (0, record [0])
        f_name_edit.insert (0, record [1])
        l_name_edit.insert (0, record [2])
        Gender_edit.insert (0, record [3])
        DOJi_edit.insert (0, record [4])
    def edit ():
        connection = sqlite3.connect ("myTable.db")
        crsr = connection.cursor()
        crsr.execute ( """ UPDATE emp SET staff_number = :staffnum, fname = :f_name, lname = :l_name, Geneder = :Gender, joining = :DOJi Where oid = :Aid""",
                       {
                           "staffnum" :  Staffno_edit.get(),
                           "f_name" :  f_name_edit.get(),
                           "l_name" :  l_name_edit.get(),
                           "Gender" :  Gender_edit.get(),
                           "DOJi" :  DOJi_edit.get(),
                           "Aid" :  deli.get()
                       }
                    )
        connection.commit()
        connection.close()
        
    Button (up , text = "Submit Changes" , command = edit).grid (row = 5 , column = 1 , pady = 10, padx = 10)
    Button (up , text = "Exit" , command = up.destroy).grid (row = 6 , column = 1 , pady = 10, padx = 10)
    connection.commit()
    connection.close()
Button (root, text = "Select the entered ID", command = update).grid(row = 9, columnspan = 2 , pady =10 , padx = 20 , ipadx = 100)


root.mainloop()
                                                                    




































        

