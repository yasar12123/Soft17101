import os
import re
path = r'C:\Users\yh28\PycharmProjects\Python Project'
fileQQ = 'quiz questions.txt'
fullPath = os.path.join(path, fileQQ)
quizQuestions = open(fullPath, encoding='utf-8')

try:
    for line in quizQuestions:
        if "Question" in line:
            print(line)
finally:
    quizQuestions.close()