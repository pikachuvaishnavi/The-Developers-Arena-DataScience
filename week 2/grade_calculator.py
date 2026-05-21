# Student Grade Calculator
# Week 2 Internship Task

print("===================================")
print("     STUDENT GRADE CALCULATOR")
print("===================================\n")

# Function to calculate grade and message
def calculate_grade(marks):

    if marks >= 90:
        grade = "A"
        message = "Excellent work! Keep shining! 🌟"

    elif marks >= 80:
        grade = "B"
        message = "Very Good! Keep it up! 👍"

    elif marks >= 70:
        grade = "C"
        message = "Good job! You can do even better! 😊"

    elif marks >= 60:
        grade = "D"
        message = "Nice effort! Keep practicing! 📚"

    else:
        grade = "F"
        message = "Don't give up! Practice makes progress! 💪"

    return grade, message


# Taking student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:

    marks = int(input("Enter marks (0-100): "))

    if marks >= 0 and marks <= 100:
        break

    else:
        print("❌ Invalid marks! Please enter marks between 0 and 100.\n")


# Calling function
grade, message = calculate_grade(marks)

# Displaying result
print("\n===================================")
print(f"      RESULT FOR {student_name.upper()}")
print("===================================\n")

print(f"Marks  : {marks}/100")
print(f"Grade  : {grade}")
print(f"Message: {message}")

print("\n Thank you for using the Grade Calculator ✨")