import os
from datetime import datetime

#This section lists paths and files
path = r'C:\Users\yh28\PycharmProjects\Python Project'
fileQuiz = 'quiz questions.txt'
fileScores = 'quizScores.txt'
quizFullPath = os.path.join(path, fileQuiz)
scoresFullPath = os.path.join(path, fileScores)
try:
    quiz = open(quizFullPath, "r")
    quizScores = open(scoresFullPath, "a")
except:
    raise FileNotFoundError("File not found, check if the files and directory exits")

#print(quiz.readlines()[2:5])

def ReadLineFromTo(path, fileName, start, end) :
    filePathOpen = open(path+'\\'+fileName, "r")
    filelines = filePathOpen.read().split("\n")
    filelines2 = filePathOpen.read().split(": ")
    startWord = str(start)
    endWord = str(end)
    startLineCount = 0
    endLineCount = 0





    for SW, filelines in enumerate(filelines):
        if startWord in filelines.split("\n"):
            startLineCount = SW + 1
            print("Word \"{}\" found in line {}".format(startWord, SW + 1))
            print(filelines.split("\n"))
            print(startLineCount)
        elif endWord in filelines:
            endLineCount = SW + 1
            print("Word \"{}\" found in line {}".format(endWord, SW + 1))
            print(filelines)
            print(endLineCount)
            break



    return

ReadLineFromTo(r'C:\Users\yh28\PycharmProjects\Python Project', 'quiz questions.txt', "Question 2", "correct:")