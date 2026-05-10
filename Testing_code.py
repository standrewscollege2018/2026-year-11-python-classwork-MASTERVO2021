#getting the sqlite3 library
import sqlite3

#define database we will be working with
#if the database does not exist, it will be created automatically
DATABASE = 'students.db'

#connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#checking results
#making a loop so it keeps running until they quit
#rn stands for run program
rp = True
while rp == True:
    try:
        #making the menu
        print("Welcome to student database")
        print("=" * 30)
        print()
        print("Select what type of query you want to run")
        print("1. Search for student by name")
        print("2. Search for student by tutor group")
        print("3. Search for student by year group")
        print("4. Quit")
        select = int(input(""))
        if select == 1:
            search = input("Enter search: ")
            search = "%"+search+"%"
            cursor.execute("SELECT * FROM student WHERE first_name LIKE ?, OR last_name LIKE ?", (search,))
            results = cursor.fetchall()
            print(f"{'Name'}:20 {'Tutor group'}")
            print("=" * 30)
            #set a counter, ln stands for list number
            ln = 1
            for result in results:
                print(f"{ln}.  {result[1]} {result[2]} - {result[3]:10}")
                ln = ln + 1
            ln = ln - 1
            print("=" * 30)
            print (f"{ln} result(s) found")
            print("Enter number to see all information, or enter 0 to return to main menu")
            option = int(input(""))
            if option == 0:
                ln = 1
            else:
                ln + 1
    except ValueError:
        print("That is not a option")

