student_grades = []
students = 0
passed = 0

while True:
    grade_input = int(input("Enter a Grade: "))
    
    if grade_input <= 39 or grade_input >= 100:
        print(str("Invalid Input. Must be between 40 and 100."))
        break
    
    else:
        students +=1
        student_grades.append(int(grade_input))
        
        grade_average = sum(student_grades) / len(student_grades)
    
        if grade_input >= 75:
            passed += 1
            
    confirmation = input("Enter Another Grade? (Y/N): ")
    
    if confirmation.lower() == "n":
        
        average = sum(student_grades)/students
        print(f"**Average Grade: {average:.2f}%")
        print(f"**No. of Students Passed: {passed}")
        
        passing_percentage = passed/students*100
        print(f"**Passing Percentage: {passing_percentage:.2f}%")
        break
        
    elif confirmation.lower() == "y":
        continue
    
    else:
        print("Invalid Input. Must be between 40 and 100.")