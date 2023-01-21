#Write a program to iterate and in each iteration, print the sum of the current and previous number

number_start = int(input("Input number: "))
number_of_iterations = int(input("How many number of times do you want to iterate: "))
prev_number = (number_start - 1)

for number_loop in range(number_of_iterations):
    print("The sum of current number " + str(number_start) + " and previous number " + str(prev_number) + " is " + str(number_start + prev_number))
    number_start += 1
    prev_number += 1

