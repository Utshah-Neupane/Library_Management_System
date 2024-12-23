
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
def checkout():
    submit_conn = sqlite3.connect('LibraryManagementSystem.db')
    submit_cur = submit_conn.cursor()

#(BOOK_ID, BRANCH_ID, CARD_NO, DATE_OUT, DUE_DATE, RETURNED_DATE) 

    # Insert into BOOK_LOANS
    submit_cur.execute('''INSERT INTO BOOK_LOANS
        VALUES(?,?,?,?,?,?,?)''',
        (
            book_id.get(),
            branch_id.get(),
            card_no.get(),
            date_out.get(),
            due_date.get(),
            returned_date.get(),
            returned_late.get()
        ))



    # Update BOOK_COPIES
    submit_cur.execute('''UPDATE BOOK_COPIES
        SET NO_OF_COPIES = NO_OF_COPIES - 1
        WHERE BOOK_ID = ? AND BRANCH_ID = ?''',
        (
            book_id.get(),
            branch_id.get()
        ))



    # Fetch updated records
    submit_cur.execute('''SELECT BOOK_ID, BRANCH_ID, NO_OF_COPIES
        FROM BOOK_COPIES
        WHERE BOOK_ID = ? AND BRANCH_ID = ?''',
        (
            book_id.get(),
            branch_id.get()
        ))


    records = submit_cur.fetchall()
 
    print_records = "\n\n\n\nUpdated book copies\n"

    for record in records:
        print_records += ("Book ID: " + str(record[0]) +
                          ", Branch ID: " + str(record[1]) +
                          ", No of Copies: " + str(record[2]) + "\n")

    print(print_records)


    result_label = Label(root, text = print_records)
    result_label.grid(row = 10, column = 0, columnspan = 5)
	

    submit_conn.commit()
    submit_conn.close()





#define all the GUI components on the tkinter root window
#place your wdgets: place / grid / pack


book_id = Entry(root, width = 30)
book_id.grid(row = 0, column = 1, padx = 40)   #everthing below will be padded as well

branch_id = Entry(root, width = 30)
branch_id.grid(row = 1, column = 1)

card_no = Entry(root, width = 30)
card_no.grid(row = 2, column = 1)

date_out = Entry(root, width = 30)
date_out.grid(row = 3, column = 1)

due_date = Entry(root, width = 30)
due_date.grid(row = 4, column = 1)

returned_date = Entry(root, width = 30)
returned_date.grid(row = 5, column = 1)

returned_late = Entry(root, width = 30)
returned_late.grid(row = 6, column = 1)




#define all labels for textboxes
book_id_label = Label(root, text = 'Book ID: ')
book_id_label.grid(row = 0, column = 0)

branch_id_label = Label(root, text = 'Branch ID: ')
branch_id_label.grid(row = 1, column = 0)

card_no_label = Label(root, text = 'Card No: ')
card_no_label.grid(row = 2, column = 0)

date_out_label = Label(root, text = 'Date Out(YYYY-MM-DD): ')
date_out_label.grid(row = 3, column = 0)

due_date_label = Label(root, text = 'Due Date(YYYY-MM-DD): ')
due_date_label.grid(row = 4, column = 0)  

returned_date_label = Label(root, text = 'Returned Date(YYYY-MM-DD): ')
returned_date_label.grid(row = 5, column = 0)

returned_late_label = Label(root, text = 'Returned Late? (0/1): ')
returned_late_label.grid(row = 6, column = 0)





#button

submit_btn = Button(root, text = 'Checkout Book', command = checkout)  
submit_btn.grid(row = 15, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


root.mainloop()