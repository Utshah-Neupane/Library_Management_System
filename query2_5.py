from tkinter import *
import sqlite3


#create tkinter window
root = Tk()
root.title ('Library Mangement System')
root.geometry('650x650')	



#connect to the DB
conn = sqlite3.connect('LibraryManagementSystem.db')

#create DB cursor
add_lms = conn.cursor()



# Define the function
def late_returned():
    submit_conn = sqlite3.connect('LibraryManagementSystem.db')
    submit_cur = submit_conn.cursor()

    # Query for late returns
    submit_cur.execute('''
        SELECT BOOK_ID, BRANCH_ID, CARD_NO, DATE_OUT, DUE_DATE, RETURNED_DATE,
        CASE 
            WHEN RETURNED_DATE IS NULL
            THEN JULIANDAY('NOW') - JULIANDAY(DUE_DATE)

            ELSE JULIANDAY(RETURNED_DATE) - JULIANDAY(DUE_DATE)
        END AS DAYS_LATE 

        FROM BOOK_LOANS
        WHERE ((JULIANDAY(RETURNED_DATE) > JULIANDAY(DUE_DATE)) OR (RETURNED_DATE IS NULL))
        AND DUE_DATE BETWEEN ? AND ?''', 
        (
        	due_start.get(), due_end.get()
        ))

    records = submit_cur.fetchall()

    print_records = "\n\n\n\n\nLate Returns:\n"
    for record in records:
        print_records += ("Book_ID: " + str(record[0]) +
                          ", Branch_ID: " + str(record[1]) +
                          ", Card No: " + str(record[2]) +
                          ", Date_Out: " + str(record[3]) +
                          ", Due_Date: " + str(record[4]) +
                          ", Returned_Date: " + str(record[5]) +
                          ", Total_late_days: " + str(record[6]) + "\n")

    print(print_records)  # Displays in terminal

    # Displays in GUI
    result_label = Label(root, text=print_records, anchor="w", justify=LEFT, wraplength=600)
    result_label.grid(row=10, column=0, columnspan=5)

    submit_conn.commit()
    submit_conn.close()



#define all the GUI components on the tkinter root window
#place your wdgets: place / grid / pack

due_start = Entry(root, width = 30)
due_start.grid(row = 0, column = 1, padx = 40)

due_end = Entry(root, width = 30)
due_end.grid(row = 1, column = 1)



#define all labels for textboxes
start_label = Label(root, text = 'Due date start: ')
start_label.grid(row = 0, column = 0)

end_label = Label(root, text = 'Due date end: ')
end_label.grid(row = 1, column = 0)




#button

submit_btn = Button(root, text = 'Late Returns', command = late_returned)  
submit_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)


root.mainloop()


