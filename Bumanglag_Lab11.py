#Initialization
student_grades = []
students = 0
passed = 0

print("\nEnter grades for the students (between 40 and 100). Type 'DONE' when finished.\n")

while True:
    #Grade input
    grade_input = input("Enter a Grade: ")

    #Checks for 'Done' input
    if grade_input.lower() == 'done':

        #Calculates the grade within the list if true
        if student_grades:

            average = sum(student_grades) / students
            print(f"\n**Average Grade: {average:.2f}%")
            print(f"**Number of Students Passed: {passed}")
            passing_percentage = (passed / students) * 100
            print(f"**Passing Percentage: {passing_percentage:.2f}%\n")

        #Otherwise, the list is empty, no grades will be computed
        else:
            print("No grades were entered.")
        break

    #Validates grade input such as those with decimals
    if grade_input.replace(".", "", 1).isdigit():
        grade_input = float(grade_input)

        #Checks if grades are within the required range
        if 40 <= grade_input <= 100:
            students += 1
            student_grades.append(grade_input)

            #Checks if the grade input has passed
            if grade_input >= 75:
                passed += 1

        #Handling for out of range input
        else:
            print("Invalid Input. Grade must be between 40 and 100.")

    #Handling for invalid input (non-numeric inputs etc.)
    else:
        print("Invalid Input. Please enter a number between 40 and 100 or 'DONE' to finish.")