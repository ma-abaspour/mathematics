
class Matrix:
    def __init__(self, data):
        if not self.is_matrix(data):
            raise ValueError("Invalid matrix.")
        self.data = data

    @staticmethod
    def is_matrix(data):
        if not isinstance(data, list) or not data:
            return False
        row_length = len(data[0])
        for row in data:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True

    @property
    def dimension(self):
        return len(self.data), len(self.data[0])

    @staticmethod
    def zero(rows, cols):
        return Matrix([[0 for _ in range(cols)] for _ in range(rows)])

    @staticmethod
    def identity(size):
        return Matrix([[1 if i == j else 0 for j in range(size)] for i in range(size)])

    @staticmethod
    def transpose(m):
        return Matrix([list(row) for row in zip(*m.data)])

    @staticmethod
    def minor(m, row, col):
        return Matrix([r[:col] + r[col+1:] for i, r in enumerate(m.data) if i != row])

    @staticmethod
    def determinant(m):
        rows, cols = m.dimension
        if rows != cols:
            raise ValueError("Matrix must be square.")
        if rows == 1:
            return m.data[0][0]
        if rows == 2:
            return m.data[0][0] * m.data[1][1] - m.data[0][1] * m.data[1][0]
        return sum((-1)**j * m.data[0][j] * Matrix.determinant(Matrix.minor(m, 0, j)) for j in range(cols))

    @staticmethod
    def inverse(m):
        rows, cols = m.dimension
        if rows != cols:
            raise ValueError("Matrix must be square.")
        det = Matrix.determinant(m)
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        cofactors = [
            [((-1) ** (i + j)) * Matrix.determinant(Matrix.minor(m, i, j)) for j in range(cols)]
            for i in range(rows)
        ]
        adjugate = Matrix.transpose(Matrix(cofactors))
        return Matrix.scalar_multiply(adjugate, 1 / det)

    @staticmethod
    def scalar_multiply(m, scalar):
        return Matrix([[x * scalar for x in row] for row in m.data])

    @staticmethod
    def rref(m):
        data = [row[:] for row in m.data]
        rows, cols = len(data), len(data[0])
        current_row = 0
        for col in range(cols):
            pivot_row = None
            for i in range(current_row, rows):
                if data[i][col] != 0:
                    pivot_row = i
                    break
            if pivot_row is None:
                continue
            if pivot_row != current_row:
                data[current_row], data[pivot_row] = data[pivot_row], data[current_row]
            pivot_value = data[current_row][col]
            data[current_row] = [x / pivot_value for x in data[current_row]]
            for i in range(rows):
                if i != current_row:
                    factor = data[i][col]
                    data[i] = [a - factor * b for a, b in zip(data[i], data[current_row])]
            current_row += 1
            if current_row == rows:
                break
        return Matrix(data)

    @staticmethod
    def rank(m):
        rref_matrix = Matrix.rref(m)
        return sum(any(abs(x) > 1e-14 for x in row) for row in rref_matrix.data)

    @staticmethod
    def dot(m1, m2):
        if m1.dimension != m2.dimension:
            raise ValueError("Dimension mismatch for dot product.")
        return sum(a * b for row1, row2 in zip(m1.data, m2.data) for a, b in zip(row1, row2))

    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimension mismatch.")
        return Matrix([[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(self.data, other.data)])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix.scalar_multiply(self, other)
        elif isinstance(other, Matrix):
            r1, c1 = self.dimension
            r2, c2 = other.dimension
            if c1 != r2:
                raise ValueError("Dimension mismatch for multiplication.")
            return Matrix([[sum(self.data[i][k] * other.data[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)])
        else:
            raise TypeError("Invalid operand type.")

    def to_vector(self):
        rows, cols = self.dimension
        if rows == 1:
            return Vector(self.data[0])
        elif cols == 1:
            return Vector([row[0] for row in self.data])
        else:
            raise ValueError("Matrix must be 1D to convert to vector.")

    def __repr__(self):
        return f"Matrix({self.data})"

    def __str__(self):
        return "\n".join(" ".join(f"{x:.2f}" for x in row) for row in self.data)



print(Matrix.identity(3))
print(Matrix.zero(2, 3))

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m3 = Matrix([[4, 3], [6, 3]])
m4 = Matrix([[4, 7], [2, 6]])
m5 = Matrix([[1, 2, -1], [-2, -3, 1], [3, 5, 0]])

print(m1)
print(Matrix.rank(m1))
print(m1 + m2)
print(m1 * 2)
print(m1 * m2)
print(Matrix.transpose(m1))
print(Matrix.determinant(m3))
print(Matrix.inverse(m4))
print(m4 * Matrix.inverse(m4))
print(Matrix.rref(m5))


# print("Solution to Ax = b:")
A = Matrix([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]])
b = Matrix([[8], [-11], [-3]])
print(Matrix.inverse(A) * b)


