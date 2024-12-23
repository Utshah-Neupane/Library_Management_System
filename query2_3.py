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
# Define the submit function
def add_book():
    submit_conn = sqlite3.connect('LibraryManagementSystem.db')
    submit_cur = submit_conn.cursor()


    # Insert into BOOK
    submit_cur.execute('''INSERT INTO BOOK(TITLE, PUBLISHER_NAME)
        VALUES(?,?)''',
        (
            title.get(),
            publisher_name.get(),
        ))



    # Get book_id generated
    submit_cur.execute('''SELECT BOOK_ID 
        FROM BOOK
        WHERE TITLE = ?''',
        (
            title.get(),
        ))

    book_id_generated = submit_cur.fetchone()[0]



    # Insert into BOOK_AUTHORS
    submit_cur.execute('''INSERT INTO BOOK_AUTHORS(BOOK_ID, AUTHOR_NAME)
        VALUES(?,?)''',
        (
            book_id_generated,
            author_name.get(),
        ))



    # Insert into BOOK_COPIES for each branch
    for branch_id in range(1, 6):   #since we added two branches in part 2 of project 
        submit_cur.execute('''INSERT INTO BOOK_COPIES(BOOK_ID, BRANCH_ID, NO_OF_COPIES)
            VALUES(?,?,5)''',
            (
                book_id_generated,
                branch_id,
            ))


    # Fetch and display updated records
    submit_cur.execute('''SELECT *
        FROM BOOK_COPIES
        WHERE BOOK_ID = ?''',
        (
            book_id_generated,
        ))


    records = submit_cur.fetchall()

    print_records = "\n\n\n\n\n\nUpdated copies of book:\n"
    for record in records:
        print_records += ("Book ID: " + str(record[0]) +
                          ", Branch ID: " + str(record[1]) +
                          ", No of Copies: " + str(record[2]) + "\n")

    print(print_records)  # Displays in terminal

    # Displays in GUI
    result_label = Label(root, text=print_records)
    result_label.grid(row=10, column=0, columnspan=5)

    submit_conn.commit()
    submit_conn.close()




#define all the GUI components on the tkinter root window
#place your wdgets: place / grid / pack

title = Entry(root, width = 30)
title.grid(row = 0, column = 1)

publisher_name = Entry(root, width = 30)
publisher_name.grid(row = 1, column = 1)

author_name = Entry(root, width = 30)
author_name.grid(row = 2, column = 1, padx = 40)




#define all labels for textboxes
title_label = Label(root, text = 'Title: ')
title_label.grid(row = 0, column = 0)

publisher_name_label = Label(root, text = 'Publisher Name: ')
publisher_name_label.grid(row = 1, column = 0)

author_name_label = Label(root, text = 'Author Name: ')
author_name_label.grid(row = 2, column = 0)




#button

submit_btn = Button(root, text = 'Add New Book', command = add_book)  
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


root.mainloop()

