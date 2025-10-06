class Matrix:
    def __init__(self, matrix_string):
        self.matrix = self.insertion(matrix_string)
        
    def insertion(self, matrix_string):
        result = []
        row_len = matrix_string.split("\n")
        for row in range(len(row_len)):
            split_row = row_len[row].split(" ")
            rows = []
            for col in range(len(split_row)):
                rows.append(int(split_row[col]))
            result.append(rows)

        return result

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        columns = []
        for i in range(len(self.matrix)):
            columns.append(self.matrix[i][index-1])
        return columns
