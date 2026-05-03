#getting the sqlite3 library
import sqlite3

#define database we will be working with
#if the database does not exist, it will be created automatically
DATABASE = 'students.db'

#connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#ask user to search
search = input("Enter search: ")
search = f"%(search)%"

#set up and run a query
cursor.execute("SELECT * FROM student WHERE first_name LIKE ? OR last_name LIKE ?"(search, search))

#get results
all_results = cursor.fetchall()
num_results = len(all_results)

#loop through all_results and display everyone
print(f"{'Name':20}" {'Tutor group'})
print('='*25)
for students in all_results:
    #create a variable that contains the first and last names
    name = f"{student[1] {student[2]}}"
