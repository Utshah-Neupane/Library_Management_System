from tkinter import *
import sqlite3


# Create tkinter window
root = Tk()
root.title('Library Management System')
root.geometry('650x650')


# Connect to the DB
conn = sqlite3.connect('LibraryManagementSystem.db')


#create DB cursor
add_lms = conn.cursor()



# Define the submit function
def add_borrower():
    submit_conn = sqlite3.connect('LibraryManagementSystem.db')
    submit_cur = submit_conn.cursor()


    # Insert into BORROWER
    submit_cur.execute('''INSERT INTO BORROWER(NAME, ADDRESS, PHONE)
        VALUES(?,?,?)''',
        (
            name.get(),
            address.get(),
            phone.get()
        ))



    # Get Card_no generated
    submit_cur.execute('''SELECT CARD_NO, NAME, ADDRESS 
        FROM BORROWER
        WHERE NAME = ?''',
        (
            name.get(),
        ))


    records = submit_cur.fetchall()


    print_records = "\n\n\n\n\n\nNew added borrower card number\n"
    for record in records:
        print_records += ("Card_no: " + str(record[0]))

    print(print_records)  # Displays in terminal


    # Displays in GUI
    result_label = Label(root, text=print_records)
    result_label.grid(row=10, column=0, columnspan=5)

    submit_conn.commit()
    submit_conn.close()





#define all the GUI components on the tkinter root window
#place your wdgets: place / grid / pack

name = Entry(root, width = 30)
name.grid(row = 0, column = 1, padx = 40)

address = Entry(root, width = 30)
address.grid(row = 1, column = 1)

phone = Entry(root, width = 30)
phone.grid(row = 2, column = 1)




#define all labels for textboxes
name_label = Label(root, text = 'Borrower Name: ')
name_label.grid(row = 0, column = 0)

addr_label = Label(root, text = 'Address: ')
addr_label.grid(row = 1, column = 0)

phone_label = Label(root, text = 'Phone: ')
phone_label.grid(row = 2, column = 0)




#button

submit_btn = Button(root, text = 'Add New Borrower', command = add_borrower)  
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


root.mainloop()

