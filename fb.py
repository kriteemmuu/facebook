from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
root.geometry("500x400")
root.title("Facebook")


##creating database
conn=sqlite3.connect("facebook.db")
c=conn.cursor()
# c.execute(""" CREATE TABLE User(
#     first_name text,
#     last_name text,
#     address text,
#     age_num integer,
#     password text,
#     father_name text,
#     city text,
#     zipcode integer
#     )""")
# print("Table created succcessfully")

##To delete from records
def delete():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("DELETE from user WHERE oid = " + delete_box.get())
    print("Deleted successfully")    
    conn.commit()
    conn.close()

##To update records
def update():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    
    c.execute("""UPDATE user SET 
            first_name=:first,
            last_name=:last,
            address=:address,
            age_num=:ages,
            password=:password,
            father_name=:f_name,
            city=:city,
            zipcode=:zipcode
    
            WHERE oid =:oid""",
             {
              "first":f_name_editor.get(),
              "last":l_name_editor.get(),
              "address":address_editor.get(),
              "ages":age_num_editor.get(),
              "password":password_editor.get(),
              "f_name":father_name_editor.get(),
              "city":city_editor.get(),
              "zipcode":zipcode_editor.get(),
              "oid":record_id
            } 
        )
    messagebox.showinfo("kryss","updated successfully")
    conn.commit()
    conn.close()

##To edit records
def edit():
    global editor
    editor=Toplevel()
    editor.title("update data")
    editor.geometry("300x400")
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM user WHERE  oid =" + record_id)
    records = c.fetchall()
    
    global f_name_editor
    global l_name_editor
    global address_editor
    global age_num_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zipcode_editor
    
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=10)
    
    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1)
    
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1)
    
    age_num_editor=Entry(editor,width=30)
    age_num_editor.grid(row=3,column=1)
    
    password_editor=Entry(editor,width=30)
    password_editor.grid(row=4,column=1)
    
    father_name_editor=Entry(editor,width=30)
    father_name_editor.grid(row=5,column=1)
    
    city_editor=Entry(editor,width=30)
    city_editor.grid(row=6,column=1)
    
    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=7,column=1)
    
    f_name_label=Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    
    l_name_label=Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)
    
    address_label=Label(editor,text="Address")
    address_label.grid(row=2,column=0)
    
    age_label=Label(editor,text="Age")
    age_label.grid(row=3,column=0)
    
    password_label=Label(editor,text="Password")
    password_label.grid(row=4,column=0)
    
    fatherName_label=Label(editor,text="Father Name")
    fatherName_label.grid(row=5,column=0)
    
    city_label=Label(editor,text="City")
    city_label.grid(row=6,column=0)
    
    zipcode_label=Label(editor,text="Zip Code")
    zipcode_label.grid(row=7,column=0)
    
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        age_num_editor.insert(0,record[3])
        password_editor.insert(0,record[4])
        father_name_editor.insert(0,record[5])
        city_editor.insert(0,record[6])
        zipcode_editor.insert(0,record[7])
        
    edit_btn= Button(editor,text="save",command=update)
    edit_btn.grid(row=10,columnspan=2,padx=10,pady=10,ipadx=125)
    conn.commit()
    conn.close()
        
##To show data 
def query():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("SELECT *,oid FROM user")
    
    records=c.fetchall()
    # print(records)
    
    print_records=''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' '+ str(record[3])+ ' ' + '\t'+str(record[8])+"\n" 
    
    query_label=Label(root,text=print_records)
    query_label.grid(row=11,column=0,columnspan=2)
    
    conn.commit()
    conn.close()

##To submit
def submit():
    conn=sqlite3.connect("facebook.db")
    c=conn.cursor()
    c.execute("INSERT INTO user values(:first_name, :last_name, :address ,:age, :password, :father_name,:city, :zipcode)",{
        "first_name":first_name.get(),
        "last_name":last_name.get(),
        "address":address.get(),
        "age":age_num.get(),
        "password":password.get(),
        "father_name":father_name.get(),
        "city":city.get(),
        "zipcode":zipcode.get()
        } )
    
    messagebox.showinfo("kryss", "Inserted successfully")
    conn.commit()
    conn.close()

##creating entry to insert data
first_name= Entry(root, width=20)
first_name.grid(row=0,column=1)

last_name=Entry(root,width=20)
last_name.grid(row=1,column=1)

address=Entry(root,width=20)
address.grid(row=2,column=1)

age_num=Entry(root,width=20)
age_num.grid(row=3,column=1)

password=Entry(root,width=20)
password.grid(row=4,column=1)

father_name=Entry(root,width=20)
father_name.grid(row=5,column=1)

city=Entry(root,width=20)
city.grid(row=6,column=1)

zipcode=Entry(root,width=20)
zipcode.grid(row=7,column=1)

delete_box=Entry(root,width=20)
delete_box.grid(row=8,column=1)

##creating entry label
label_f_name=Label(root,text="First Name:")
label_f_name.grid(row=0,column=0)

label_l_name=Label(root,text="Last Name:")
label_l_name.grid(row=1,column=0)

label_address=Label(root,text="Address:")
label_address.grid(row=2,column=0)


label_age=Label(root,text="Age:")
label_age.grid(row=3,column=0)

label_pass=Label(root,text="Password:")
label_pass.grid(row=4,column=0)

label_father_name=Label(root,text="Father Name:")
label_father_name.grid(row=5,column=0)

label_city=Label(root,text="City:")
label_city.grid(row=6,column=0)

label_zipcode=Label(root,text="Zip code:")
label_zipcode.grid(row=7,column=0)

delete_label=Label(root,text="delete:")
delete_label.grid(row=8,column=0)


##for button
btn=Button(root,text="Submit",command=submit)
btn.grid(row=17,column=1)

query_btn=Button(root, text="Show Records",command=query)
query_btn.grid(row=15,column=0,columnspan=2,padx=10,pady=10,ipadx=90)

edit_btn=Button(root,text="Update",command=edit)
edit_btn.grid(row=14,column=0,columnspan=2,padx=10,pady=10,ipadx=107)

delete_btn=Button(root,text="Delete",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=110)


conn.commit()
conn.close()
root.mainloop()
