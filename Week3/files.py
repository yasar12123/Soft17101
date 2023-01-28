import os
path = r'C:\Users\yh28\PycharmProjects\Python Project'
filename = 'pg1342.txt'
prideAndPrejudice = os.path.join(path, filename)
my_file = open(prideAndPrejudice, encoding='utf-8')
countChapter = 0

try:
    for line in my_file:
        if "CHAPTER" in line:
            countChapter += 1
            print(line)
    print("There are %d chapters" %countChapter)

finally:
    my_file.close()