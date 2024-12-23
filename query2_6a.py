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



def search_borrower():
    submit_conn = sqlite3.connect('LibraryManagementSystem.db')
    submit_cur = submit_conn.cursor()

    # Prepare the base SQL query with optional filters
    base_query = '''
    SELECT CARD_NO AS Borrower_ID,
           BORROWER_NAME AS Name,
           CASE
               WHEN LATE_FEE_BALANCE IS NULL OR LATE_FEE_BALANCE = 0 THEN '$0.00'
               ELSE '$' || printf('%.2f', LATE_FEE_BALANCE)
           END AS Late_Fee_Balance
    FROM VBOOK_LOAN_INFO
    WHERE 1 = 1
    '''

    # Filters for borrower ID or name
    params = []
    if borrower_id.get():
        base_query += " AND CARD_NO = ?"
        params.append(borrower_id.get())
    if borrower_name.get():
        base_query += " AND BORROWER_NAME LIKE ?"
        params.append(f"%{borrower_name.get()}%")

    # If no filters are provided, order by balance amount
    if not params:
        base_query += " ORDER BY LATE_FEE_BALANCE DESC"

    submit_cur.execute(base_query, params)
    records = submit_cur.fetchall()

    # Display results in the GUI
    print_records = "\nBorrower Details:\n"
    for record in records:
        print_records += f"Borrower ID: {record[0]}, Name: {record[1]}, Late Fee Balance: {record[2]}\n"

    result_label = Label(root, text=print_records, anchor="w", justify=LEFT, wraplength=750)
    result_label.grid(row=10, column=0, columnspan=5)

    submit_conn.close()


# Define the function to list book information

def search_books():
    submit_conn = sqlite3.connect('LibraryManagementSystem.db')
    submit_cur = submit_conn.cursor()

    # Prepare the base SQL query with optional filters
    base_query = '''
    SELECT BOOK_ID AS Book_ID,
           BOOK_TITLE AS Title,
           CASE
               WHEN LATE_FEE_BALANCE IS NULL THEN 'Non-Applicable'
               ELSE '$' || printf('%.2f', LATE_FEE_BALANCE)
           END AS Late_Fee
    FROM VBOOK_LOAN_INFO
    WHERE 1 = 1
    '''

    # Filters for borrower ID, book ID, or part of the book title
    params = []
    if borrower_id.get():
        base_query += " AND CARD_NO = ?"
        params.append(borrower_id.get())
    if book_id.get():
        base_query += " AND BOOK_ID = ?"
        params.append(book_id.get())
    if book_title.get():
        base_query += " AND BOOK_TITLE LIKE ?"
        params.append(f"%{book_title.get()}%")

    # If no filters are provided, order by highest remaining late fee
    if not params:
        base_query += " ORDER BY LATE_FEE DESC"

    submit_cur.execute(base_query, params)
    records = submit_cur.fetchall()

    # Display results in the GUI
    print_records = "\nBook Information:\n"
    for record in records:
        print_records += f"Book ID: {record[0]}, Title: {record[1]}, Late Fee: {record[2]}\n"

    result_label = Label(root, text=print_records, anchor="w", justify=LEFT, wraplength=750)
    result_label.grid(row=15, column=0, columnspan=5)

    submit_conn.close()




# GUI Components for borrower search
borrower_id = Entry(root, width=30)
borrower_id.grid(row=0, column=1, padx=20)

borrower_name = Entry(root, width=30)
borrower_name.grid(row=1, column=1, padx=20)


#labels
borrower_id_label = Label(root, text='Borrower ID: ')
borrower_id_label.grid(row=0, column=0)

borrower_name_label = Label(root, text='Borrower Name (or Part of Name): ')
borrower_name_label.grid(row=1, column=0)

#button
borrower_search_btn = Button(root, text='Search Borrower', command=search_borrower)
borrower_search_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=100)




# GUI Components for book search
book_id = Entry(root, width=30)
book_id.grid(row=5, column=1, padx=20)

book_title = Entry(root, width=30)
book_title.grid(row=6, column=1, padx=20)


#labels
book_id_label = Label(root, text='Book ID: ')
book_id_label.grid(row=5, column=0)

book_title_label = Label(root, text='Book Title (or Part of Title): ')
book_title_label.grid(row=6, column=0)


#buttons
book_search_btn = Button(root, text='Search Books', command=search_books)
book_search_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


root.mainloop()
