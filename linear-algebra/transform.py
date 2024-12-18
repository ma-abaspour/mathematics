
from matrix import Matrix
import math


class Transform:
    def __init__(self, matrix):
        if not isinstance(matrix, Matrix):
            raise ValueError("Transform must be initialized with a Matrix.")
        self.matrix = matrix

    @staticmethod
    def scaling_2d(sx, sy):
        return Transform(Matrix([
            [sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]
        ]))

    @staticmethod
    def scaling_3d(sx, sy, sz):
        return Transform(Matrix([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ]))

    @staticmethod
    def rotation_2d(theta):
        return Transform(Matrix([
            [math.cos(theta), -math.sin(theta), 0],
            [math.sin(theta), math.cos(theta), 0],
            [0, 0, 1]
        ]))

    @staticmethod
    def rotation_3d(axis, theta):
        if axis == 'x':
            return Transform(Matrix([
                [1, 0, 0, 0],
                [0, math.cos(theta), -math.sin(theta), 0],
                [0, math.sin(theta), math.cos(theta), 0],
                [0, 0, 0, 1]
            ]))
        elif axis == 'y':
            return Transform(Matrix([
                [math.cos(theta), 0, math.sin(theta), 0],
                [0, 1, 0, 0],
                [-math.sin(theta), 0, math.cos(theta), 0],
                [0, 0, 0, 1]
            ]))
        elif axis == 'z':
            return Transform(Matrix([
                [math.cos(theta), -math.sin(theta), 0, 0],
                [math.sin(theta), math.cos(theta), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]))
        else:
            raise ValueError("Invalid axis. Choose from 'x', 'y', or 'z'.")

    @staticmethod
    def translation_2d(tx, ty):
        return Transform(Matrix([
            [1, 0, tx],
            [0, 1, ty],
            [0, 0, 1]
        ]))

    @staticmethod
    def translation_3d(tx, ty, tz):
        return Transform(Matrix([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ]))

    def compose(self, other):
        if not isinstance(other, Transform):
            raise ValueError("Can only compose with another Transform.")
        return Transform(self.matrix * other.matrix)

    def inverse(self):
        return Transform(Matrix.inverse(self.matrix))

    def apply(self, point):
        """Apply the transform to a point (2D or 3D)."""
        if len(point) + 1 != self.matrix.dimension[0]:
            raise ValueError("Point dimensionality does not match transform.")
        # Convert point to homogeneous coordinates
        homogeneous_point = Matrix([point + [1]])
        transformed_point = self.matrix * Matrix.transpose(homogeneous_point)
        # Convert back to Cartesian coordinates
        return [x / transformed_point.data[-1][0] for x in transformed_point.data[:-1][0]]

    def __repr__(self):
        return f"Transform({repr(self.matrix)})"

    def __str__(self):
        return str(self.matrix)


# scaling = Transform.scaling_2d(2, 3)
# rotation = Transform.rotation_2d(math.pi / 4)
# combined = scaling.compose(rotation)
# print("Combined Transform (Scaling + Rotation):")
# print(combined)

# point = [1, 1]
# print("Point after Transformation:")
# print(combined.apply(point))

# translation = Transform.translation_3d(5, 7, 10)
# rotation = Transform.rotation_3d('z', math.pi / 2)
# combined = translation.compose(rotation)
# print("Combined 3D Transform (Translation + Rotation):")
# print(combined)

# point_3d = [1, 2, 3]
# print("3D Point after Transformation:")
# print(combined.apply(point_3d))

# print("Inverse of Combined Transform:")
# print(combined.inverse())
