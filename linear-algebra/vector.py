
from matrix import Matrix

class Vector:
    def __init__(self, data):
        if not isinstance(data, list) or len(data) == 0:
            raise ValueError("Vector must be a non-empty list.")
        self.data = data

    @property
    def dimension(self):
        return len(self.data)

    def dot(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimension mismatch.")
        return sum(a * b for a, b in zip(self.data, other.data))

    def norm(self):
        return sum(x**2 for x in self.data) ** 0.5

    def angle_with(self, other):
        """Compute the angle (in radians) between two vectors."""
        dot_product = self.dot(other)
        norm_product = self.norm() * other.norm()
        if norm_product == 0:
            raise ValueError("Cannot compute angle with a zero vector.")
        import math
        return math.acos(dot_product / norm_product)

    def cross(self, other):
        if self.dimension != 3 or other.dimension != 3:
            raise ValueError("Cross product only defined for 3D vectors.")
        x1, y1, z1 = self.data
        x2, y2, z2 = other.data
        return Vector([
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2
        ])

    def projection_onto(self, other):
        """Project this vector onto another vector."""
        norm_other = other.norm()
        if norm_other == 0:
            raise ValueError("Cannot project onto a zero vector.")
        scalar_projection = self.dot(other) / norm_other
        return other * (scalar_projection / norm_other)

    def as_matrix(self):
        """Convert the vector to a column matrix."""
        return Matrix([[x] for x in self.data])

    def __add__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimension mismatch.")
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise ValueError("Dimension mismatch.")
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Can only multiply by a scalar.")
        return Vector([x * scalar for x in self.data])

    def __repr__(self):
        return f"Vector({self.data})"

    def __str__(self):
        return f"({', '.join(map(str, self.data))})"

def gram_schmidt(vectors):
    """Perform Gram-Schmidt orthogonalization on a list of Vectors."""
    orthogonal = []
    for v in vectors:
        for u in orthogonal:
            proj = u * (v.dot(u) / u.dot(u))  # Properly use Vector operations
            v = v - proj  # Subtract projection
        orthogonal.append(v)
    return orthogonal


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([1, 0, 0])
v4 = Vector([0, 1, 0])

print("Vector v1:", v1)
print("Vector v2:", v2)
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 3 =", v1 * 3)
print("v1 . v2 =", v1.dot(v2))
print("||v1|| =", v1.norm())
print("v3 x v4 =", v3.cross(v4))
print("Angle between v1 and v2 (radians):", v1.angle_with(v2))
print("Projection of v1 onto v2:", v1.projection_onto(v2))

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
orthonormal_basis = gram_schmidt([v1.as_matrix(), v2.as_matrix()])
print("Orthonormal Basis:")
for vec in orthonormal_basis:
    print(vec)