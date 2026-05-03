#getting the sqlite3 library
import sqlite3

#define database we will be working with
#if the database does not exist, it will be created automatically
DATABASE = 'students.db'

#connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#select names from student table
cursor.execute("SELECT student_id, first_name, last_name, tutor_group FROM student")
results = cursor.fetchall()

#counting results
number_of_results = len(results)
for result in results:
    print(f"{result[0]} - {result[1]:10} {result[2]:15} {result[3]:3}")
