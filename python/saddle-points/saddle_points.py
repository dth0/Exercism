def saddle_points(matrix):

    result = []
    if len(matrix) == 0:
        return []

    column_size = len(matrix[0])

    for row in range(1, len(matrix)):
        if column_size != len(matrix[row]):
            raise ValueError("Invalid Matrix")

    max_value = [max(row) for row in matrix]

    for x in range(column_size):

        columns = [row[x] for row in matrix]
        colum_min = min(columns)

        for y in range(len(max_value)):

            if colum_min == max_value[y]:
                result.append(
                    {
                        "row": y+1,
                        "column": x+1
                    }
                )

    return result
