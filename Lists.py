ka = True
while ka == True:
    guess = int((input("How many questions do you think you will get right (Put capital letters at the start of you answer)")))
    if guess > 10 or guess < 0:
        print("That is not a number between 0 to 10. Grow a brain")
    else:
        ka = False
