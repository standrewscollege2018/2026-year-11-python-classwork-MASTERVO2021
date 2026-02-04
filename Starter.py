'''This program demostrates print(), data types, variables, unput and f-strings'''

#print() is a function that outputs whatever is inside the brackets
#numbers can be included directly in the brackets
print(123)

#when printing text, it must be in speechmarks which turn into a string
print("hello")

#there are lots of different types of data types
#Intigers, decimals (floating point numbers)
#text (strings), boolean (true or false)

#use variable to store information
name = "Pluto"
first_name = "John"
last_name = "Smith"
age = 24

#you can inclise variables inside print() statements
print(name)
#To combine variables with a string, we use f-string
#the variable goes inside curly brackets {}
print(f"my dog is called {name} and he is {age} years old")

#we use input() to get input from the use
user_name = input("What is your name?")
print(f"hello {user_name}")

#Print hello to the user and ask them how old they are
print(f"Hello {user_name}")
input("how old are you?")
