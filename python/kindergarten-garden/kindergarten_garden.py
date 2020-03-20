class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            self._students = [
                "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"
            ]
        else:
            self._students = sorted(students)

        self._diagram = diagram.splitlines()

        self._plants = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

    def plants(self, student):
        result = []

        try:
            index = self._students.index(student) * 2

            for plants in self._diagram:
                first = plants[index]
                second = plants[index+1]

                result.append(self._plants[first])
                result.append(self._plants[second])

        except ValueError:
            return []

        return result
