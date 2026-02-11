'''Program to see if patient needs tablets'''
Age = int(input("What is your age in years?"))

#Making sure the age is valid
if Age<0 or Age>50:
    print("Invalid data. Please insert a number between 1-50")
else:
    #Checking age
    if Age >= 12:
        print("Take 2 tablets")
    else: 
        print("Measure your weight")
        Weight = int(input("What is your weight?"))
        MG = Weight * 10
        print(f"Take {MG}mg")
