def add_student(name, grades):
  name = name.capitalize()
  students[name] = grades

def update_grades(name, grades):
  name = name.capitalize()
  if name in students:
    students[name].extend(grades)

def calculate_average(name):
  name = name.capitalize()
  if name in students:
    return sum(students[name]) / len(students[name])

def print_students_with_averages():
  for name, grades in students.items():
    avg = calculate_average(name)
    print(f"{name.capitalize()} - Average: {avg:.2f}")

def sort_students_by_grades():
  student_list = list(students.items())
  n = len(student_list)
  for i in range(n):
    for j in range(0, n-i-1):
        avg1 = sum(student_list[j][1]) / len(student_list[j][1])
        avg2 = sum(student_list[j+1][1]) / len(student_list[j+1][1])
        if avg1 < avg2:
          student_list[j], student_list[j+1] = student_list[j+1], student_list[j]
  for name, grades in student_list:
    avg = sum(grades) / len(grades)
    print(f"{name.capitalize()} - Average: {avg:.2f}")

students={}
n=int(input('Enter the number of students: '))
for i in range(n):
  name=input('Enter the name of the student: ')
  grades=input('Enter the grades of the student: ')
  grades=grades.split(" ")
  grades=[int(grade) for grade in grades]
  add_student(name, grades)

print('----------')
print_students_with_averages()
print('----------')
sort_students_by_grades()