def saddle_points(matrix):
    if not matrix:
        return []

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")
    candidates = []
    for row in range(len(matrix)):
        max_ = max(matrix[row])
        for col in range(len(matrix[row])):
            min_ = min([matrix[i][col] for i in range(len(matrix))])
            if matrix[row][col] == min_ and matrix[row][col] == max_:
                candidates.append({'column': col+1, 'row': row+1})
                
    return candidates
