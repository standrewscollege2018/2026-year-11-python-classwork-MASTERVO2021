#Making variables for later
ka = True
score = 0
answers = ["Yes", "Fruit", "Before", "Cereal", "No scope", "Yes", "No", "Yes", "No", "Yes"]
questions = ["Question 1: Does pineapple belong on pizza?","Question 2: Is tomato a fruit or vegtable?","Question 3: Do you brush your teeth before or after you eat?","Question 4: Do you pour milk or cereal first?", "Question 5: What comes after 360?", "Question 6: Is this quiz good?", "Question 7: Is 67 the best number?", "Question 8: Is starcraft a dead game?", "Question 9: Do you wear socks with sandals/slippers? (yes no question)", "Question 10: Am i good at making quizes?"]
quiz = True
qn = 0
an = 0
#Getting their name
print("What is your name?")
name = input("")
while name.strip() == "":
    print("Name cannot be blank. Insert your name")
    name = input("")
#Asking for questions
print("There will be 10 questions")
#Getting a valid number guess
while ka == True:
    print("How many questions do you think you will get right (Put capital letters at the start of you answer)")
    guess = int(input(""))
    if guess > 10 or guess < 0:
        print("That is not a number between 0 to 10.")
    else:
        ka = False
ka = True
#Printing questions
while ka == True:
    print(questions [qn])
    q = input("")
    if q == answers [an]:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print(f"The correct answer was {answers [an]}")
    qn += 1
    an += 1
    if qn == 10:
        ka = False
#Comparing the score
if guess < score:
    print(f"Congratulations {name}, Your score was higher than your guess, which was {guess}. You got {score}/10")
if score > guess:
    print(f"Sorry {name}, Your score was lower than your guess, which was {guess}. You got {score}/10")
if score == guess:
    print(f"Congratulations {name}, Your score was the same as your guess, which was {guess}. You got {score}/10")



