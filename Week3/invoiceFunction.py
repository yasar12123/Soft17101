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


def getLineFromTo(file, start, end):
    fileOpen = open(file), "r"
    filelines = fileOpen.read().split("\n")
    StartLine = str(start)
    EndLine = str(end)
    for i, filelines in enumerate(filelines):
        if StartLine in filelines.split():
            print("Word \"{}\" found in line {}".format(StartLine, i + 1))

getLineFromTo(quiz, "question 1", "dff")