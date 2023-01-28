
numberOfStudents = int(input("Number of Students: "))
studentGrade = []
count = 0

for studentGradeLoop in range(numberOfStudents):
    count += 1
    studentGrade.append(input("Grade for student" + str([count]) + ": "))

total = sum([float(x) for x in studentGrade])
average = total / studentGradeLoop

print("The total scores is: ", sum([float(x) for x in studentGrade]))
print("The Average is: ", average)