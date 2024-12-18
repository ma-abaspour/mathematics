




from matrix import Matrix
from vector import gram_schmidt

def power_iteration(A, num_iter=100, tol=1e-10):
    rows, cols = A.dimension
    if rows != cols:
        raise ValueError("Matrix must be square.")
    b = Matrix([[1] for _ in range(rows)])
    for _ in range(num_iter):
        b_next = A * b
        b_next = b_next * (1 / b_next.to_vector().norm())
        if (b_next - b).to_vector().norm() < tol:
            break
        b = b_next
    eigenvalue = (A * b).data[0][0] / b.data[0][0]
    return eigenvalue, b.to_vector()

def qr_decomposition(A):
    rows, cols = A.dimension
    vectors = [Matrix([[A.data[row][i]] for row in range(rows)]).to_vector() for i in range(cols)]
    Q = gram_schmidt(vectors)
    R = [[q.dot(Matrix([[A.data[row][j]] for row in range(rows)]).to_vector()) if i <= j else 0 for j in range(cols)] for i, q in enumerate(Q)]
    return Matrix([q.data for q in Q]), Matrix(R)

def qr_iteration(A, num_iter=100, tol=1e-10):
    rows, cols = A.dimension
    if rows != cols:
        raise ValueError("Matrix must be square.")
   





A = Matrix([[4, 1], [1, 3]])

# print("Largest Eigenvalue and Eigenvector:")
# eigenvalue, eigenvector = power_iteration(A)
# print(eigenvalue)
# print(eigenvector)

# print("QR Decomposition:")
# Q, R = qr_decomposition(A)
# print(Q)
# print(R)

print("All Eigenvalues (QR Iteration):")
eigenvalues = qr_iteration(A)
print(eigenvalues)
