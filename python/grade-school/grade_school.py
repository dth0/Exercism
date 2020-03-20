from collections import defaultdict


class School:
    def __init__(self):
        self._grades = defaultdict(list)

    def add_student(self, name, grade):
        self._grades[grade].append(name)

    def roster(self):
        students = []
        for grade in sorted(self._grades.keys()):
            students_list = self._sort_data(self._grades[grade])
            students.extend(students_list)

        return students

    def grade(self, grade_number):
        return self._sort_data(self._grades[grade_number])

    @staticmethod
    def _sort_data(data):
        return sorted(data)
