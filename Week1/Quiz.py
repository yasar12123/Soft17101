totalScore = 0
correctAnswer = "\nThat is the correct answer"
incorrectAnswer = "\nThat is the wrong answer"
attemptCounter = 0

while (attemptCounter < 3):
    q1 = input("\nWhat is the capital of the United Kingdom? \n A.London \n B.Paris \n C.Washington \n D.Madrid \n \n What is your answer? ")
    q1_upper = q1.upper()

    if q1_upper == "A":
        print(correctAnswer)
        totalScore += 1
        break
    else:
        print(incorrectAnswer)
        attemptCounter += 1
        print("Attempt Number: ", attemptCounter)

attemptCounter = 0

while (attemptCounter < 3):
    q2 = input("\nWhat is the most widely used currency in the European continent? \n A.Pound \n B.Euro \n C.Dollar \n D.Rand \n \n What is your answer? " )
    q2_upper = q2.upper()

    if q2_upper == "B":
        print(correctAnswer)
        totalScore += 1
        break

    else:
        print(incorrectAnswer)
        attemptCounter += 1
        print("Attempt Number: ", attemptCounter)

attemptCounter = 0

while (attemptCounter < 3):
    q3 = input("\nWhat Colour is the grass? \n A.Blue \n B.Yellow \n C.Green \n D.Red \n \n What is your answer? " )
    q3_upper = q3.upper()

    if q3_upper == "C":
        print(correctAnswer)
        totalScore += 1
        break

    else:
        print(incorrectAnswer)
        attemptCounter += 1
        print("Attempt Number: ", attemptCounter)

print("\nYour total score is ", totalScore)
