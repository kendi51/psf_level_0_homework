def finding_the_percentage(students, query):
    # create an average variable
    # create a variable storing the sum of grades
    # divide the sum by the length and place it in the average variable
    # print the average

    # create an average variable
    average = 0
    grades_list = students[query]
    # create a variable storing the sum of grades
    total_grades_score = sum(grades_list)
    # divide the sum by the length and place it in the average variable
    average = total_grades_score / len(grades_list)
    # print the average
    print(f"{average:.2f}")


students = {"Harsh": [25, 26.6, 28], "Anurag": [26, 28, 30], "Mary": [52, 56, 60]}
finding_the_percentage(students, "Harsh")
