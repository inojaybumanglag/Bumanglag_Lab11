student_grades = []
students = 0
passed = 0

print("\nEnter grades for the students (between 40 and 100). Type 'DONE' when finished.\n")

while True:
    grade_input = input("Enter a Grade: ")

    if grade_input.lower() == 'done':

        if student_grades:

            average = sum(student_grades) / students
            print(f"\n**Average Grade: {average:.2f}%")
            print(f"**Number of Students Passed: {passed}")
            passing_percentage = (passed / students) * 100
            print(f"**Passing Percentage: {passing_percentage:.2f}%\n")

        else:
            print("No grades were entered.")
        break

    if grade_input.replace(".", "", 1).isdigit():
        grade_input = float(grade_input)

        if 40 <= grade_input <= 100:
            students += 1
            student_grades.append(grade_input)

            if grade_input >= 75:
                passed += 1
        else:
            print("Invalid Input. Grade must be between 40 and 100.")
    else:
        print("Invalid Input. Please enter a number between 40 and 100 or 'DONE' to finish.")