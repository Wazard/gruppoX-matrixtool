class MatrixHandler:
    def __init__(self, data: list[list[float]]):
        self.data = data

    def print(self):
        # Print the matrix in a readable format.
        for row in self.data:
            print(" ".join(str(val) for val in row))

    def validate(self):
        if not self.data:
            return False # Matrix is empty

        # Check row lengths
        row_length = len(self.data[0])
        for row in self.data:
            if len(row) != row_length:
                return False  # Matrix rows are not of equal length.

        # Check element types
        for row in self.data:
            for val in row:
                if not isinstance(val, (int, float)):
                    return False # Matrix has different value types other than numeric

        return True # Valid

    def __repr__(self):
        return f"MatrixHandler(rows={len(self.data)}, cols={len(self.data[0]) if self.data else 0})"

""" 
matrix1 = MatrixHandler([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = MatrixHandler([[1, 2], [3, 4, 5]])  # invalid

print("Matrix 1:")
matrix1.print_matrix()
print(f"Matrix is {('invalid','valid')[matrix1.validate()]}")

print("\nMatrix 2:")
matrix2.print_matrix()
print(f"Matrix is {('invalid','valid')[matrix2.validate()]}") """