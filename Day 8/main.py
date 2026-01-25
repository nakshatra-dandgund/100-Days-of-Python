"""
Day 16 Practice Project
Student Result & Performance Analyzer
100 Days of Code - python
Author: Nakshatra Dandgund
"""

# Taking user input
name = input("Enter student name: ")
marks = []

# Taking marks for 3 subjects
for i in range(1, 4):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculations
total_marks = sum(marks)
percentage = (total_marks / 300) * 100

# Display student details
print("\n---------- Student Result ----------")
print("Name (Uppercase):", name.upper())
print("Name (Title Case):", name.title())

# Display subject-wise marks
for i in range(len(marks)):
    print(f"Subject {i+1} marks:", marks[i])

print("------------------Report Card------------------")
print("Total Marks:", total_marks)
print(f"Percentage: {percentage:.2f}%")

# Match-case for performance evaluation
match percentage:
    case p if p >= 90:
        performance = "Excellent Performance"
    case p if p >= 75:
        performance = "Very Good Performance"
    case p if p >= 60:
        performance = "Good Performance"
    case p if p >= 40:
        performance = "Average Performance"
    case _:
        performance = "Fail"

print("Performance:", performance)
