
numberOfStudents = int(input("Number of Students: "))
studentGrade = []
count = 0

for studentGradeLoop in range(numberOfStudents):
    count+=1
    studentGrade.append(input("Grade for student" + str([count]) + ": " ))

total = sum([float(x) for x in studentGrade])
average = total / studentGradeLoop

print("Here are the total scores ", sum([float(x) for x in studentGrade]))
print("Here is the average ", average )