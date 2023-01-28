import os
from datetime import datetime

#This section lists paths and files
path = r'C:\Users\yh28\PycharmProjects\Python Project'
fileQuiz = 'quiz.txt'
fileScores = 'quizScores.txt'
quizFullPath = os.path.join(path, fileQuiz)
scoresFullPath = os.path.join(path, fileScores)
quiz = open(quizFullPath, "w")
quizScores = open(scoresFullPath, "a")

#all questions in the quiz
numberOfQuestions = 3
questionCounter = 1
question1 = ('\n' "What is the capital of United Kingdom?" +
             '\n' "A.London" +
             '\n' "B.Paris" +
             '\n' "C.Washington" +
             '\n' "D.Madrid")

question2 = ('\n' "What is the most widely used currency in the European continent?" +
             '\n' "A.Pound" +
             '\n' "B.Euro" +
             '\n' "C.Dollar" +
             '\n' "D.Rand")

question3 = ('\n' "Who is the main actor in the Mission Impossible movies?" +
             '\n' "A.Daniel Craig" +
             '\n' "B.Tom Cruise" +
             '\n' "C.Mr Bean" +
             '\n' "D.James Bond")

#answers for the questions above in order
questionAnswerList = ["A", "B", "B"]
questionAnswerListCounter = 0

#
attemptCounter = 0
totalScore = 0


#start of the program
userName = input("What is your name? ")

for quizLoop in range(numberOfQuestions):
    while attemptCounter < 3:
        question = input(eval(("question%s" % questionCounter)))
        q_upper = question.upper()

        if q_upper == questionAnswerList[questionAnswerListCounter]:
            print("\nThat is the correct answer")
            totalScore += 1
            break
        else:
            print("\nThat is the wrong answer")
            attemptCounter += 1
            print("Attempt Number: ", attemptCounter)

    quiz.write('\n' + eval(("question%s" % questionCounter)) +
               '\n' "The correct answer is: %s" % questionAnswerList[questionAnswerListCounter])
    questionCounter += 1
    questionAnswerListCounter += 1
    attemptCounter = 0

print("\nYour total score is ", totalScore)
#end of program


#write scores to file and close any open files
quiz.close()
quizScores.write('\n' 'Player: {} ; Score: {} ; DateTime: {}' .format(userName, totalScore, datetime.now()))
quizScores.close()
