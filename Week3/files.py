import os

try:
    path = r'C:\Users\yh28\PycharmProjects\Python Project'
    filename = 'pg1342.txt'
    prideAndPrejudice = os.path.join(path, filename)
    my_file = open(prideAndPrejudice, encoding='utf-8')
except:
    raise FileNotFoundError("The file can not be found, ensure that the directory and file name are correct")

countChapter = 0
try:
    for line in my_file:
        if "CHAPTER" in line.upper():
            countChapter += 1
            print(line)
    print("There word chapters occurs %d times" %countChapter)

finally:
    my_file.close()
