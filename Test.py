#Making the intro sections before the questions start
name = input("What is your name?")
print("There will be 10 questions")
guess = input("How many questions do you think you will get right (Put capital letters at the start of you answer)")
score = 0
answers = ["Yes", "Fruit", "Before", "cereal", "No scope", "Yes", "No", "Yes", "No", "Yes"]
questions = ["Question 1: Does pineapple belong on pizza?","Question 2: Is tomato a fruit or vegtable?","Question 3: Do you brush your teeth before or after you eat?","Question 4: Do you pour milk or cereal first?", "Question 5: What comes after 360?", "Question 6: Is this quiz good?", "Question 7: Is 67 the best number?", "Question 8: Is starcraft a dead game?", "Question 9: Do you wear socks with sandals/slippers? (yes no question)", "Question 10: Am i good at making quizes?"]
quiz = True
#Making questions

print(questions [0])
q1 = input("")
if q1 == answers [0]:
    print("🍍")
    score += 1
else:
    print("DISGRACE TO HUMANITY")

print(questions [1])
q2 = input("")
if q2 == answers [1]:
    print("🍅")
    score += 1
else:
    print("WRONG")

print(questions [2])
q3 = input("")
if q3 == answers [2]:
    print("🪥")
    score += 1
else:
    print("Yes, i know everything tastes weird but WRONG")

print(questions [3])
q4 = input("")
if q4 == answers [3]:
    print("Why milk, the cereal will splash the milk out...")
    score += 1
else:
    print("🥛✖️")

print(questions [4])
q5 = input("")
if q5 == answers [4]:
    print("( -_•)▄︻デ══━一")
    score += 1
else:
    print("Not a true gamer (or you don't game at all)")

print(questions [5])
q6 = input("")
if q6 == answers [5]:
    print("👍")
    score += 1
else:
    print("😢")

print(questions [6])
q7 = input("")
if q7 == answers [6]:
    print("🤡➡️  6️⃣7️⃣")
    score += 1
else:
    print("Steal a brainrot main 100%")

print(questions [7])
q8 = input("")
if q8 == answers [7]:
    print("Good")
    score += 1
else:
    print("YANG GET OUT WE ALL KNOW IT'S YOU PUTTING NO")

print(questions [8])
q9 = input("")
if q9 == answers [8]:
    print("🩴+🧦=💣")
    score += 1
else:
    print("Why...")

print(questions [9])
q10 = input("")
if q10 == answers [9]:
    print("👍")
    score += 1
else:
    print("😢")

print(f"Congratulations {name}, you got guessed {guess} questions, and you got {score} right")





