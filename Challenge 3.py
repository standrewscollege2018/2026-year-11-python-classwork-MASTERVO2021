'''Challenge 3'''

total = 0

while total < 200:
    num1 = int(input("Enter a number between 50 and 100"))


    if num1 > 100 or num1 < 50:
        print("That number is not between 50 and 100")
    else:
        total += num1
print(total)
