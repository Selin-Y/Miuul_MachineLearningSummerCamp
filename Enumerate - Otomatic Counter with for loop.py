# Enumerate - Otomatic Counter/Indexer with for loop

# 1. Question:
students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

# 2. Question:
students = ["John", "Mark", "Venessa", "Mariam"]
A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)