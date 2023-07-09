class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def print_matrix(self):
        """
        Метод выводит матрицу на печать.
        """
        for row in self.data:
            print(row)

    def __eq__(self, other):
        """
        Метод для сравнения двух матриц.

        Args:
            other (Matrix): Другая матрица для сравнения.

        Returns:
            bool: True, если матрицы равны. False, если матрицы не равны.
        """
        if self.rows != other.rows or self.columns != other.columns:
            return False

        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != other.data[i][j]:
                    return False

        return True

    def __add__(self, other):
        """
        Метод для сложения двух матриц.

        Args:
            other (Matrix): Другая матрица для сложения.

        Returns:
            Matrix: Результат сложения матриц.
        """
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions for addition")

        result = Matrix(self.rows, self.columns)

        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result

    def __mul__(self, other):
        """
        Метод для умножения двух матриц.

        Args:
            other (Matrix): Другая матрица для умножения.

        Returns:
            Matrix: Результат умножения матриц.
        """
        if self.columns != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix")

        result = Matrix(self.rows, other.columns)

        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[i][k]

        return result

# Пример использования класса Matrix
matrix1 = Matrix(2, 3)
matrix1.data = [[1, 2, 3], [4, 5, 6]]

matrix2 = Matrix(2, 3)
matrix2.data = [[7, 8, 9], [10, 11, 12]]

# Вывод матрицы на печать
matrix1.print_matrix()

# Сравнение двух матриц
if matrix1 == matrix2:
    print("Matrices are equal")
else:
    print("Matrices are not equal")

# Сложение двух матриц
result_matrix = matrix1 + matrix2
result_matrix.print_matrix()

# Умножение двух матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

result_matrix2 = matrix1 * matrix3
result_matrix2.print_matrix()
