students = {
    "Aman": 78,
    "Riya": 92,
    "Kriti": 88,
    "Rahul": 95
}

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Highest Scorer:", highest, "-", students[highest])
print("Lowest Scorer:", lowest, "-", students[lowest])

print("\nStudents scoring more than 85 marks:")
for name, marks in students.items():
    if marks > 85:
        print(name, "-", marks)
