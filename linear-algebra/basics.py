
def dimension(matrix):
  return tuple([len(matrix), len(matrix[-1])])

def zero(column, row):
  # return [[0]*column]*row
  return [[0] * column for i in range(row)]

def identity(column, row):
  matrix = zero(column, row)
  for i in range(row):
    for j in range(column):
      if i == j:
        matrix[i][j] = 1
  return matrix

def transpose(matrix):
  return list(map(list, zip(*matrix)))

def minor(matrix, row, col):
  return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

def determinant(matrix):
  # Base case for 2x2 matrix
  if len(matrix) == 2 and len(matrix[0]) == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

  # Recursive case
  det = 0
  for col in range(len(matrix)):
    det += ((-1) ** col) * matrix[0][col] * determinant(minor(matrix, 0, col))
  return det

def add(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def scalar_multiply(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]

def multiply(matrix1, matrix2):
    result = zero(len(matrix2[0]), len(matrix1))
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        return None
    size = len(matrix)
    cofactors = []
    for r in range(size):
        cofactor_row = []
        for c in range(size):
            minor_det = determinant(minor(matrix, r, c))
            cofactor_row.append(((-1) ** (r + c)) * minor_det)
        cofactors.append(cofactor_row)
    adjugate = transpose(cofactors)
    return [[adjugate[i][j] / det for j in range(size)] for i in range(size)]

