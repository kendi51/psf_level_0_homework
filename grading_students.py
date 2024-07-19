def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    # loop throu the grades
    for grade in grades:
        # - if grade < 38
        if grade < 38:
            # - return grade as is
            rounded_grades.append(grade)
        # - else
        else:
            # - find the next muliple of 5 from the grade (multiple)
            # - we add 5 to the grade and store in (total)
            total = grade + 5
            # - find all the numbers between grand and total
            for num in range(total):
                # - take the first number that is divisable by 5
                if num % 5 == 0:
                    multiple = num
                    break
            # - store (difference) the difference between (multiple) and grade
            difference = multiple - grade
            # - check if (d) < 3
            if difference < 3:
                # - if true: return (multiple)
                rounded_grades.append(multiple)
            else:
                # - if false: return grade
                rounded_grades.append(grade)
    # return rounded list
    return rounded_grades


print(gradingStudents([73, 67, 38, 33]))
