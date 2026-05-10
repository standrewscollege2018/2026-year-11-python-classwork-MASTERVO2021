'''Challenge 2'''
num1 = int(input("Enter a number"))
num2 = int(input("Enter a bigger number"))
while num1 > num2:
    print("That is not a bigger number")
    num2 = int(input("Enter a bigger number"))
    print(f"number 1 and 2 are {num1} and {num2}")  