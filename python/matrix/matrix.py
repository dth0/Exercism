class Matrix:
    def __init__(self, matrix_string):
        self._matrix = []

        for line in matrix_string.splitlines():
            row = [int(x) for x in line.split()]
            self._matrix.append(row)

    def row(self, index):
        return self._matrix[index-1]

    def column(self, index):
        return [self._matrix[x][index-1] for x in range(len(self._matrix))]
