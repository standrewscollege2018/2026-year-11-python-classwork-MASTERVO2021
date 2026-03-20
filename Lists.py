ka = True
while ka == True:
    try:
        guess = int(input("Enter number between 0-10"))
        ka = False
    except ValueError:
        print("Invalid answer")