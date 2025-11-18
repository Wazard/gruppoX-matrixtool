from MatrixHandler import MatrixHandler as Handler

class StatisticEvaluator(Handler):
    def find_max(self):
        max_val = None
        for row in self.data:
            curr = max(row)
            if max_val is None or curr > max_val:
                max_val = curr
        return max_val

    def get_row_average(self, row: int):
        # get the row
        row_data = self.data[row]
        # compute average: sum / len
        return sum(row_data)/len(row_data)

""" 
matrix = MatrixHandler([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
stats = StatisticEvaluator(matrix.data)


print("Matrix:")
stats.print_matrix()
print("Validation:", stats.validate()) # validation: True
print("Max value:", stats.find_max()) # 9

print("Row 0 average:", stats.get_row_average(0))  # (1+2+3)/3 = 2.0
print("Row 1 average:", stats.get_row_average(1))  # (4+5+6)/3 = 5.0
print("Row 2 average:", stats.get_row_average(2))  # (7+8+9)/3 = 8.0 """