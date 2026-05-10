#getting the sqlite3 library
import sqlite3

#define database we will be working with
#if the database does not exist, it will be created automatically
DATABASE = 'students.db'

#connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#making the menu
#options
print("Welcome to student database")
print("=" * 30)
print("")
print("Select what type of query you want to run")
print("1. Search for student by name")
print("2. Search for student by tutor group")
print("3. Search for student by year group")
print("4. Quit")

#checking results
#making a loop so it keeps running until they quit
#rn stands for run program
run_program = True
while run_program == True:
    #ka stands for keep asking
    try:
        select = int(input(""))
        if select == 1 or select == 2 or select == 3 or select == 4:
            if select == 4:
              print("Sucessfully quit")
            if select == 1:
                search = input("Enter search: ")
                search = "%"+search+"%"
                cursor.execute("SELECT * FROM student WHERE first_name LIKE ?", (search,))
                results = cursor.fetchall()
                for result in results:
                    print(result[1])
            if select == 2:
                search = input("Enter search: ")
                search = "%"+search+"%"
                cursor.execute("SELECT * FROM student WHERE tutor_code LIKE ?", (search,))
                results = cursor.fetchall()
                for result in results:
                    print(result[3])
            if select == 3:
                search = int(input("Enter search: "))
                search = "%"+search+"%"
                cursor.execute("SELECT * FROM student WHERE year_group LIKE ?", (search,))
                results = cursor.fetchall()
                for result in results:
                    print(result[5])
        else:
            print("That is not an option")
    except ValueError:
        print("That is not an option")

