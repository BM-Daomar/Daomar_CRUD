import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

    selected_item = listBox.selection()[0]
    values = listBox.item(selected_item, 'values')
    if values:
        e1.insert(0, values[0])
        e2.insert(0, values[1])
        e3.insert(0, values[2])


def Add():
    studid = e1.get()
    studname = e2.get()
    date = e3.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="attendance_list")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO registration (id, stdntname, date) VALUES (%s, %s, %s)"
       val = (studid, studname, date)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Student registered successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()

       listBox.insert("", "end", values=(studid, studname, date))

    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()



def update():
    studid = e1.get()
    studname = e2.get()
    date = e3.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="attendance_list")
    mycursor = mysqldb.cursor()

    try:
        sql = "UPDATE registration SET stdntname = %s, date = %s WHERE id = %s"
        val = (studname, date, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Information", "Record Updated successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus_set()

        selected_item = listBox.selection()[0]
        listBox.item(selected_item, values=(studid, studname, date))

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="attendance_list")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from registration where id = %s"
       val = (studid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleted successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="attendance_list")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,stdntname,date FROM registration")
        records = mycursor.fetchall()
        print(records)

        for i, (id,stname, date) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, stname, date))
            mysqldb.close()

root = Tk()
root.geometry("1000x400")
root.configure(bg="#F6E3BA")

input_frame = tk.LabelFrame(root, bg="#CFB284", padx=10, pady=10)  
input_frame.pack(side=LEFT, padx=10, pady=10)

listbox_frame = ttk.Frame(root)
listbox_frame.pack(side=LEFT, padx=10, pady=10)

tk.Label(input_frame, text="Attendance Check", bg="#CFB284", font=('Helvetica', 30, 'bold')).grid(row=0, column=0, columnspan=5)
tk.Label(input_frame, text="Student ID", bg="#CFB284").grid(row=1, column=0)
e1 = Entry(input_frame)
e1.grid(row=1, column=1)
tk.Label(input_frame, text="Full Name", bg="#CFB284").grid(row=2, column=0)
e2 = Entry(input_frame)
e2.grid(row=2, column=1)
tk.Label(input_frame, text="Date", bg="#CFB284").grid(row=3, column=0)
e3 = Entry(input_frame)
e3.grid(row=3, column=1)

Button(input_frame, text="Add", bg="#FFFCC7", command=Add, height=2, width=8).grid(row=4, column=0)
Button(input_frame, text="Update", bg="#FFFCC7", command=update, height=2, width=8).grid(row=4, column=1)
Button(input_frame, text="Delete", bg="#FFFCC7", command=delete, height=2, width=8).grid(row=4, column=2)

cols = ('Student ID', 'Student Name', 'Date')
listBox = ttk.Treeview(listbox_frame, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=0, column=0, padx=10, pady=10)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
