students = []
lecturers = []

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and \
                1 <= grade <= 10:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
            print(f'Оценка за лекцию по предмету {course} от студента {self.name} преподавателю {lecturer.name} : {grade}')
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.__average_grade__()} \n' \
               f"Курсы в процессе изучения: {','.join(self.courses_in_progress)} \n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)} \n")
        return res

    def __average_grade__(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        res = round((sum(all_grades) / len(all_grades)), 1)
        return res

    def __le__(self, other):
        if not isinstance(other, Student):
            return 'Нет такого студента'
        if self.__average_grade__() < other.__average_grade__():
            return f'{self.name} учится хуже, чем {other.name}'
        elif self.__average_grade__() > other.__average_grade__():
            return f'{self.name} учится лучше, чем {other.name}'
        else:
            return f'{self.name} и {other.name} учатся одинаково'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}
        lecturers.append(self)

    def __str__(self):
        res = (f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.__average_grade__()} \n' \
               f"Закрепленные курсы: {', '.join(self.courses_attached)} \n")
        return res

    def __average_grade__(self):
        all_grades = []
        for grade in self.lec_grades.values():
            all_grades += grade
        res = round((sum(all_grades) / len(all_grades)), 1)
        return res

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого лектора')
            return
        if self.__average_grade__() < other.__average_grade__():
            return f'{self.name} читает лекции хуже, чем {other.name}'
        elif self.__average_grade__() > other.__average_grade__():
            return f'{other.name} читает лекции хуже, чем {self.name}'
        else:
            return f'{other.name} и {self.name} читают лекции одинаково хорошо'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and \
                1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            print(f'Оценка за домашку по предмету {course} от преподавателя {self.name} студенту {student.name} : {grade}')
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f"Закрепленные курсы: {', '.join(self.courses_attached)} \n")
        return res

def all_students_average(students, course):
    grade_list = []
    for student in students:
        for lesson in student.grades:
            if lesson == course:
                grade_list.extend(student.grades[lesson])
    res = round((sum(grade_list) / len(grade_list)), 1)
    return f'Средняя оценка за домашние задания по всем студентам в рамках курса {course}: {res}'


def all_lecturers_average(lecturers, course):
    grade_list = []
    for lecturer in lecturers:
        for lecture in lecturer.lec_grades:
            if lecture == course:
                grade_list.extend(lecturer.lec_grades[lecture])
    res = round((sum(grade_list) / len(grade_list)), 1)
    return f'Средняя оценка за лекции по всем лекторам в рамках курса {course}: {res}'


ira_saunina = Student('Irina', 'Saunina', 'female')
ira_saunina.finished_courses += ['Civil law', 'Penal law']
ira_saunina.courses_in_progress += ['Python', 'Git']

nik_shubin = Student('Nikita', 'Shubin', 'male')
nik_shubin.finished_courses += ['Civil law', 'Penal law']
nik_shubin.courses_in_progress += ['Management', 'Advocacy']

dasha_gorunova = Student('Daria', 'Gorunova', 'female')
dasha_gorunova.finished_courses += ['Civil law', 'Penal law', 'Style']
dasha_gorunova.courses_in_progress += ['Management']

lector_chitalkin = Lecturer('Lector', 'Chitalkin')
lector_chitalkin.courses_attached += ['Python', 'Civil law', 'Penal law', 'Git']

anatoliy_bubnilkin = Lecturer('Anatoliy', 'Bubnilkin')
anatoliy_bubnilkin.courses_attached += ['Management', 'Advocacy', 'Style']

gosha_proveryalkin = Reviewer('Georgiy', 'Proveryalkin')
gosha_proveryalkin.courses_attached += ['Civil law', 'Advocacy', 'Penal law']

dima_domashkin = Reviewer('Dmitriy', 'Domashkin')
dima_domashkin.courses_attached += ['Management', 'Style', 'Python', 'Git']


dima_domashkin.rate_hw(ira_saunina, 'Python', 8)
dima_domashkin.rate_hw(ira_saunina, 'Python', 10)
dima_domashkin.rate_hw(ira_saunina, 'Python', 5)
dima_domashkin.rate_hw(ira_saunina, 'Git', 3)
dima_domashkin.rate_hw(ira_saunina, 'Git', 9)
dima_domashkin.rate_hw(ira_saunina, 'Git', 6)

dima_domashkin.rate_hw(nik_shubin, 'Management', 9)
dima_domashkin.rate_hw(nik_shubin, 'Management', 8)
dima_domashkin.rate_hw(nik_shubin, 'Management', 4)
dima_domashkin.rate_hw(nik_shubin, 'Management', 5)

gosha_proveryalkin.rate_hw(nik_shubin, 'Advocacy', 10)
gosha_proveryalkin.rate_hw(nik_shubin, 'Advocacy', 10)

dima_domashkin.rate_hw(dasha_gorunova, 'Management', 3)
dima_domashkin.rate_hw(dasha_gorunova, 'Management', 8)
dima_domashkin.rate_hw(dasha_gorunova, 'Management', 9)


ira_saunina.rate_lec(lector_chitalkin, 'Python', 10)
ira_saunina.rate_lec(lector_chitalkin, 'Python', 5)
ira_saunina.rate_lec(lector_chitalkin, 'Python', 4)
ira_saunina.rate_lec(lector_chitalkin, 'Git', 8)
ira_saunina.rate_lec(lector_chitalkin, 'Git', 3)
ira_saunina.rate_lec(lector_chitalkin, 'Git', 1)

nik_shubin.rate_lec(anatoliy_bubnilkin, 'Advocacy', 5)
nik_shubin.rate_lec(anatoliy_bubnilkin, 'Advocacy', 7)
nik_shubin.rate_lec(anatoliy_bubnilkin, 'Advocacy', 6)
nik_shubin.rate_lec(anatoliy_bubnilkin, 'Management', 5)
nik_shubin.rate_lec(anatoliy_bubnilkin, 'Management', 6)
nik_shubin.rate_lec(anatoliy_bubnilkin, 'Management', 10)

dasha_gorunova.rate_lec(anatoliy_bubnilkin, 'Management', 10)
dasha_gorunova.rate_lec(anatoliy_bubnilkin, 'Management', 3)
dasha_gorunova.rate_lec(anatoliy_bubnilkin, 'Management', 6)
print()

print(ira_saunina >= nik_shubin)
print(lector_chitalkin <= anatoliy_bubnilkin)
print()

print(all_students_average(students, 'Management'))
print(all_lecturers_average(lecturers, 'Git'))
print()

print(ira_saunina)
print()
print(dima_domashkin)
print()
print(lector_chitalkin)
print()