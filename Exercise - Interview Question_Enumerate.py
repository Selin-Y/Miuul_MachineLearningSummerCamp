# Exercise - Interview Question_Enumerate
# Write a divide_students function.
# Put the students in the double index into a list.
# Take the students in one index to another list.
# But let these two lists return as a single list.

students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 ==0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

student = divide_students(students)
student[0]
student[1]