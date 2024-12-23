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
def loaned_copies():
    submit_conn = sqlite3.connect('LibraryManagementSystem.db')
    submit_cur = submit_conn.cursor()


    # Count copies loaned per branch
    submit_cur.execute('''SELECT LB.BRANCH_NAME, COUNT(*) AS COPIES_LOANED 
        FROM BOOK B NATURAL JOIN BOOK_LOANS BL
        NATURAL JOIN LIBRARY_BRANCH LB
        WHERE B.TITLE = ?
        GROUP BY LB.BRANCH_NAME''',
        (
            title.get(),
        ))


    records = submit_cur.fetchall()

    print_records = "\n\n\n\n\nCopies loaned by Branch:\n"
    for record in records:
        print_records += ("Branch Name: " + record[0] +
                          ", Copies Loaned: " + str(record[1]) + "\n")

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



#define all labels for textboxes
title_label = Label(root, text = 'Title: ')
title_label.grid(row = 0, column = 0)




#button

submit_btn = Button(root, text = 'List loaned copies per branch', command = loaned_copies)  
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


root.mainloop()

