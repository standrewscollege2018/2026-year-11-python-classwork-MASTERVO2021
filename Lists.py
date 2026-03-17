ka = True
answers = ["Yes", "Fruit", "Before", "cereal", "No scope", "Yes", "No", "Yes", "No", "Yes"]
questions = ["Question 1: Does pineapple belong on pizza?","Question 2: Is tomato a fruit or vegtable?","Question 3: Do you brush your teeth before or after you eat?","Question 4: Do you pour milk or cereal first?", "Question 5: What comes after 360?", "Question 6: Is this quiz good?", "Question 7: Is 67 the best number?", "Question 8: Is starcraft a dead game?", "Question 9: Do you wear socks with sandals/slippers? (yes no question)", "Question 10: Am i good at making quizes?"]
score = 0
while ka == True:
    print(questions [0])
    q1 = input("")
    if q1 == answers [0]:
        print("Correct")
        score += 1
    else:
        print("Wrong")
    answers += 1
    questions += 1