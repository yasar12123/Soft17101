import os
import re
path = r'C:\Users\yh28\PycharmProjects\Python Project'
filename = 'pg1342.txt'
prideAndPrejudice = os.path.join(path, filename)

##pattern = r"CHAPTER.\."
countChapter = 0

try:
    my_file = open(prideAndPrejudice, encoding='utf-8')

    for line in my_file:
        #if re.findall(pattern, line):
        if "CHAPTER" in line:
            countChapter += 1
            print(line)

finally:
    my_file.close()