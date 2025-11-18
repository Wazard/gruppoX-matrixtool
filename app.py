# Import classes from your modules, with aliases for convenience
from MatrixHandler import MatrixHandler as Handler
from MatrixFilter import MatrixFilter as Filter
from StatisticElavuator import StatisticEvaluator as Eval


def matrix_mul(matrix_1: Handler, matrix_2: Handler):
    # Validate both matrices
    if not matrix_1.validate() or not matrix_2.validate():
        raise ValueError("Invalid matrix structure")

    rows_1, cols_1 = len(matrix_1.data), len(matrix_1.data[0])
    rows_2, cols_2 = len(matrix_2.data), len(matrix_2.data[0])

    # Check multiplication compatibility
    if cols_1 != rows_2:
        raise ValueError("Matrix dimensions do not align for multiplication")

    # Optionally rectify (ReLU) both matrices before multiplication
    Filter(matrix_1.data).rectificate()
    Filter(matrix_2.data).rectificate()

    # Perform multiplication
    result = [[0] * cols_2 for _ in range(rows_1)]
    for i in range(rows_1):
        for j in range(cols_2):
            for k in range(cols_1):
                result[i][j] += matrix_1.data[i][k] * matrix_2.data[k][j]

    return Handler(result)


# Define the main entry point function
def main():
    # Create three matrices using the Handler class
    # matrix: contains negative values
    matrix = Handler([[1, -2, 3], [4, 5, -6], [6, 12, 29]])
    # matrix1: a valid rectangular matrix
    matrix1 = Handler([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # matrix2: invalid because rows have different lengths
    matrix2 = Handler([[1, 2], [3, 4, 5]])

    # Print the original matrix
    print("Original matrix:")
    matrix.print()

    # Apply rectification (turn negatives into 0) using Filter
    f = Filter(matrix.data)
    f.rectificate()
    print("\nRectified matrix:")
    f.print()

    # Use StatisticEvaluator to compute statistics on the matrix
    s = Eval(matrix.data)
    print("\nMax value:", s.find_max())
    print("Row 0 average:", s.get_row_average(0))

    # Show matrix1 and validate it
    print("Matrix 1:")
    matrix1.print()
    # validate() returns True/False, so we map it to 'valid'/'invalid'
    print(f"Matrix is {('invalid','valid')[matrix1.validate()]}")

    # Show matrix2 and validate it (expected invalid)
    print("\nMatrix 2:")
    matrix2.print()
    print(f"Matrix is {('invalid','valid')[matrix2.validate()]}")

    # Demonstrate Filter again on the original matrix
    filter = Filter(matrix.data)

    print("Original matrix:")
    filter.print()

    # Rectify the matrix (negatives → 0)
    filter.rectificate()
    print("\nRectified matrix:")
    filter.print()

    # Flatten the matrix into a single list
    print("\nFlattened matrix:", filter.flatten())

    # Demonstrate StatisticEvaluator again
    stats = Eval(matrix.data)

    print("Matrix:")
    stats.print()
    # Validate the matrix structure
    print("Validation:", stats.validate())
    # Find the maximum value
    print("Max value:", stats.find_max())

    # Compute row averages
    print("Row 0 average:", stats.get_row_average(0))
    print("Row 1 average:", stats.get_row_average(1))
    print("Row 2 average:", stats.get_row_average(2))


    matrix1 = Handler([[1,2,3],[4,5,6]])
    matrix2 = Handler([[7,8],[9,10],[11,12]])
    matrix_mul(matrix1,matrix2).print()

if __name__ == "__main__":
    main()