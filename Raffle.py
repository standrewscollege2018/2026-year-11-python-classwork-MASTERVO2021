'''Raffle'''

people = []
amount = int(0)
import random
Asking = True
while Asking == True:
    Person = input("Enter a name")
    people.append(Person)
    amount + int(1)
    if Person == "end":
        Asking = False

print(amount)

