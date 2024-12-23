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

