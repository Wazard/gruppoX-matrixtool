from MatrixHandler import MatrixHandler as Handler
from MatrixFilter import MatrixFilter as Filter
from StatisticElavuator import StatisticEvaluator as Eval

def main():
    matrix = Handler([[1, -2, 3], [4, 5, -6], [6, 12, 29]])
    matrix1 = Handler([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = Handler([[1, 2], [3, 4, 5]])

    print("Original matrix:")
    matrix.print_matrix()

    f = Filter(matrix.data)
    f.rectificate()
    print("\nRectified matrix:")
    f.print_matrix()

    s = Eval(matrix.data)
    print("\nMax value:", s.find_max())
    print("Row 0 average:", s.get_row_average(0))

    print("Matrix 1:")
    matrix1.print_matrix()
    print(f"Matrix is {('invalid','valid')[matrix1.validate()]}")

    print("\nMatrix 2:")
    matrix2.print_matrix()
    print(f"Matrix is {('invalid','valid')[matrix2.validate()]}")

    filter = Filter(matrix.data)

    print("Original matrix:")
    filter.print_matrix()

    filter.rectificate()
    print("\nRectified matrix:")
    filter.print_matrix()

    print("\nFlattened matrix:", filter.flatten())

    stats = Eval(matrix.data)

    print("Matrix:")
    stats.print_matrix()
    print("Validation:", stats.validate())
    print("Max value:", stats.find_max())

    print("Row 0 average:", stats.get_row_average(0))
    print("Row 1 average:", stats.get_row_average(1))
    print("Row 2 average:", stats.get_row_average(2))

if __name__ == "__main__":
    main()