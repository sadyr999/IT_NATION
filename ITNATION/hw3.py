studentsList = [{'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
                {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
                {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
                {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
                {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
                {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'},
                {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
                {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
                {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
                {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
                {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
                {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
                {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
                {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'},
                {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
                {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
                {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
                {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
                {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
                {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
                {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
                {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
                {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
                {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
                {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
                {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
                {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
                {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
                {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
                {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
                {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
                {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
                {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'},
                {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
                {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
                {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
                {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
                {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'}, ]

# TASK 1
totalStudents = 0
totalMale = 0
totalFemale = 0
for student in studentsList:
    totalStudents = totalStudents + 1
    if student['gender'] == 'Male':
        totalMale = totalMale + 1
    elif student['gender'] == 'Female':
        totalFemale = totalFemale + 1
    else:
        print(f"Incorrect input for {student['name']}")
print("---TASK 1 PART 1---")
print(
    f"In the group {round(totalFemale / totalStudents * 100)}% of Female students and {round(totalMale / totalStudents * 100)}% of Male students")

print("---TASK 1 PART 2---")
print("Following is the list of students attending Python")
for student in studentsList:
    if student['course'] == 'python':
        print(f"{student['name']} {student['age']} {student['gender']}")
print("---TASK 1 PART 3---")
no_duplic = []
for student in studentsList:
    if student not in no_duplic:
        no_duplic.append(student)
    else:
        print(
            f"We delete the following duplicate from the list: {student['name']} {student['age']} {student['gender']}")
print("---TASK 1 PART 4---")
totalStudents = 0
totalAbove30 = 0
for student in studentsList:
    totalStudents = totalStudents + 1
    if student['age'] >= 30:
        totalAbove30 = totalAbove30 + 1
        print(f"The following student is above 30: {student['name']} {student['age']} {student['gender']}")
print(f"In the group {round(totalAbove30 / totalStudents * 100)}% of students are above 30")
print("---TASK 1 PART 5---")
sortNames = []
sortAges = []
sortGenders = []
sortCourses = []
for student in studentsList:
    sortNames.append(student["name"])
    sortAges.append(student["age"])
    sortGenders.append(student["gender"])
    sortCourses.append(student["course"])
sortCourses.sort()
sortAges.sort()
sortNames.sort()
sortGenders.sort()
print("Following is the list of sorted names")
print(sortNames)
print("Following is the list of sorted ages")
print(sortAges)
print("Following is the list of sorted genders")
print(sortGenders)
print("Following is the list of sorted courses")
print(sortCourses)

print("---TASK 1 PART 6---")
for student in studentsList:
    if student["course"].lower() == 'javascript':
        student['course'] = 'python'
        print(f"The following student is switched to python: {student['name']} {student['age']} {student['gender']}")
    else:
        pass
print("---TASK 1 PART 7---")
newStudents = [{'name': 'Aidin', 'age': 22, 'course': 'java', 'gender': 'Male'},
               {'name': 'Almaz', 'age': 28, 'course': 'java', 'gender': 'Male'},
               {'name': 'Aziz', 'age': 21, 'course': 'java', 'gender': 'Male'},
               {'name': 'Aidin', 'age': 22, 'course': 'java', 'gender': 'Male'},
               {'name': 'Aidina', 'age': 22, 'course': 'java', 'gender': 'Female'},
               {'name': 'Aibek', 'age': 11, 'course': 'python', 'gender': 'Male'},
               {'name': 'Anton', 'age': 20, 'course': 'python', 'gender': 'Male'},
               {'name': 'Damir', 'age': 25, 'course': 'python', 'gender': 'Male'},
               {'name': 'Alima', 'age': 30, 'course': 'python', 'gender': 'Female'},
               {'name': 'Alim', 'age': 40, 'course': 'python', 'gender': 'Male'}]
for newStudent in newStudents:
    studentsList.append(newStudent)
    print(f"The following student is added: {newStudent['name']} {newStudent['age']} {newStudent['gender']} {newStudent['course']}")

for student in studentsList:
    if student["age"] < 15:
        print(f"The following student is deleted: {student['name']} {student['age']} {student['gender']}")
        student.clear()
print("---TASK 2 PART 1---")
password_list = ['password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567']
print(password_list)
while True:
    input_data = input("Password input: ")
    if input_data in password_list:
        break
    else:
        continue
print("---TASK 3 PART 1---")
for i in range(22, 88, 8):
    print(i, end = " >> ")
print("")
print("---TASK 3 PART 2---")
for i in range(1, 58):
    print(i, "I Love Python", end = " >> ")
print("")
print("---TASK 3 PART 3---")
counter = 1
while True:
    print(counter, "I Love Python", end = " >> ")
    if counter == 57:
        break
    counter += 1
print("")
print("---TASK 3 PART 4---")
c = 1
while c != 58:
    print(c, "I Love Python", end = " >> ")
    c += 1
