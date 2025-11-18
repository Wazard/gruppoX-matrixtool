class MatrixHandler:
    def __init__(self, data: list[list[float]]):
        self.data = data

    def print_matrix(self):
        # Print the matrix in a readable format.
        for row in self.data:
            print(" ".join(str(val) for val in row))

    def is_valid(self):
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