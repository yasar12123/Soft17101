

grade_score = input("What is your Grade: ")

grade_list = ["Zero", "Low Fail", "Mid Fail", "Marginal Fail",
              "Low 3rd", "Mid 3rd", "High 3rd",
              "Low 2 : 2", "Mid 2 : 2", "High 2 : 2",
              "Low 2 : 1", "Mid 2 : 1", "High 2 : 1",
              "Low 1st", "Mid 1st", "High 1st", "Exceptional 1st"]

print("You have scored a " + str(grade_list[int(grade_score)]))