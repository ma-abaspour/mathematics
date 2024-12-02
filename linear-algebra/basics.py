
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

