#Assignment (19/02/2026)
#Assignment Name: Student Data Manager
#Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades.

def student_data_manager():
    students = {}

    # Taking input for 5 students
    for i in range(5):
        name = input(f"Enter name of student {i+1}: ")
        marks = float(input(f"Enter marks of {name}: "))
        students[name] = marks

    # Calculate class average
    total_marks = sum(students.values())
    average = total_marks / len(students)

    # Find topper
    topper = max(students, key=students.get)

    print("\n--- Results ---")
    print("Class Average:", average)
    print("Topper:", topper, "-", students[topper])

    print("\n--- Grades ---")
    for name, marks in students.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print(name, ":", marks, "-", grade)


# Call the function
student_data_manager()

