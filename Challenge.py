'''Challenge'''
num1 = int(input("What is number 1?"))
num2 = int(input("What is number 2?"))
print(f"Numbers one and two are {num1} and {num2}")
if num1 > num2:
    print("Number one is bigger than number two")
if num2 > num1:
    print("Number two is bigger than number one")
if num1 == num2:
    print("Number one is the same than number two")
Sum = int(num1 + num2)
print(f"number 1 + number 2 is {Sum}")