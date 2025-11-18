# Import classes from your modules, with aliases for convenience
from MatrixHandler import MatrixHandler as Handler
from MatrixFilter import MatrixFilter as Filter
from StatisticElavuator import StatisticEvaluator as Eval

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
    matrix.print_matrix()

    # Apply rectification (turn negatives into 0) using Filter
    f = Filter(matrix.data)
    f.rectificate()
    print("\nRectified matrix:")
    f.print_matrix()

    # Use StatisticEvaluator to compute statistics on the matrix
    s = Eval(matrix.data)
    print("\nMax value:", s.find_max())
    print("Row 0 average:", s.get_row_average(0))

    # Show matrix1 and validate it
    print("Matrix 1:")
    matrix1.print_matrix()
    # validate() returns True/False, so we map it to 'valid'/'invalid'
    print(f"Matrix is {('invalid','valid')[matrix1.validate()]}")

    # Show matrix2 and validate it (expected invalid)
    print("\nMatrix 2:")
    matrix2.print_matrix()
    print(f"Matrix is {('invalid','valid')[matrix2.validate()]}")

    # Demonstrate Filter again on the original matrix
    filter = Filter(matrix.data)

    print("Original matrix:")
    filter.print_matrix()

    # Rectify the matrix (negatives → 0)
    filter.rectificate()
    print("\nRectified matrix:")
    filter.print_matrix()

    # Flatten the matrix into a single list
    print("\nFlattened matrix:", filter.flatten())

    # Demonstrate StatisticEvaluator again
    stats = Eval(matrix.data)

    print("Matrix:")
    stats.print_matrix()
    # Validate the matrix structure
    print("Validation:", stats.validate())
    # Find the maximum value
    print("Max value:", stats.find_max())

    # Compute row averages
    print("Row 0 average:", stats.get_row_average(0))
    print("Row 1 average:", stats.get_row_average(1))
    print("Row 2 average:", stats.get_row_average(2))

if __name__ == "__main__":
    main()