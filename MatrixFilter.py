from MatrixHandler import MatrixHandler

class MatrixFilter(MatrixHandler):
    def rectificate(self):
        # Replace all negative values in the matrix with 0 (ReLU).
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                self.data[row][col] = max(0, self.data[row][col])

    def flatten(self):
        # Flatten the matrix into a single list of values.
        flattened_matrix = []
        for row in self.data:
            flattened_matrix.extend(row)
        return flattened_matrix


matrix = MatrixHandler([[1, -2, 3], [-4, 5, -6], [5,2,-3]])
filter = MatrixFilter(matrix.data)

print("Original matrix:")
filter.print_matrix()

filter.rectificate()
print("\nRectified matrix:")
filter.print_matrix()

print("\nFlattened matrix:", filter.flatten())