#printing results
print("Select which trype of query you want to run")
print("1. Search for student by name")
print("2. Search for students by tutor group")

#ka stand for keep asking
ka = True
while ka == True:
    try:
        select = int(input(""))
        if select == 1 or select == 2:
            ka = False
        else:
            print("That is not an option")
    except ValueError:
        print("That is not an option")