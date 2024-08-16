my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],
    'average': None
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

my_student['average'] = average_grade(my_student)
# print(my_student)



class Student:
    def __init__(self, new_name, new_grades): # (my_object, new_name, new_grades)
        self.name = new_name # self.name ---> my_object.name
        self.grades = new_grades
    def average(self):
        return sum(self.grades) / len(self.grades)



student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('jose', [50, 60, 99, 100])
# print(Student.average(student_one))
# print(Student.average(student_one))


print(student_one.average())

