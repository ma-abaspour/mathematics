
import math

def distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def dot(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def cross(v1, v2):
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

def norm(v):
    return math.sqrt(dot(v, v))

def normalize(v):
    n = norm(v)
    return [x / n for x in v] if n != 0 else v

def translate(point, vector):
    return [p + v for p, v in zip(point, vector)]

def scale(point, factor, origin=None):
    origin = origin or [0] * len(point)
    return [origin[i] + factor * (p - origin[i]) for i, p in enumerate(point)]

def rotate(point, angle, axis='z', origin=None):
    angle = math.radians(angle)
    x, y, z = point
    origin = origin or [0, 0, 0]
    x0, y0, z0 = origin
    if axis == 'z':
        xr = x0 + math.cos(angle) * (x - x0) - math.sin(angle) * (y - y0)
        yr = y0 + math.sin(angle) * (x - x0) + math.cos(angle) * (y - y0)
        zr = z
    elif axis == 'y':
        xr = x0 + math.cos(angle) * (x - x0) + math.sin(angle) * (z - z0)
        yr = y
        zr = z0 - math.sin(angle) * (x - x0) + math.cos(angle) * (z - z0)
    elif axis == 'x':
        xr = x
        yr = y0 + math.cos(angle) * (y - y0) - math.sin(angle) * (z - z0)
        zr = z0 + math.sin(angle) * (y - y0) + math.cos(angle) * (z - z0)
    return [xr, yr, zr]

def midpoint(p1, p2):
    return [(a + b) / 2 for a, b in zip(p1, p2)]

def is_colinear(p1, p2, p3):
    v1 = [b - a for a, b in zip(p1, p2)]
    v2 = [b - a for a, b in zip(p1, p3)]
    cross_prod = cross(v1, v2)
    return all(c == 0 for c in cross_prod)

def line_intersection(p1, p2, p3, p4):
    def det(a, b, c, d):
        return a * d - b * c
    x1, y1 = p1[:2]
    x2, y2 = p2[:2]
    x3, y3 = p3[:2]
    x4, y4 = p4[:2]
    denom = det(x1 - x2, y1 - y2, x3 - x4, y3 - y4)
    if denom == 0:
        return None
    x = det(det(x1, y1, x2, y2), x1 - x2, det(x3, y3, x4, y4), x3 - x4) / denom
    y = det(det(x1, y1, x2, y2), y1 - y2, det(x3, y3, x4, y4), y3 - y4) / denom
    return [x, y]

import math

class Point:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def translate(self, vector):
        return Point(self.x + vector.x, self.y + vector.y, self.z + vector.z)

    def midpoint(self, other):
        return Point((self.x + other.x)/2, (self.y + other.y)/2, (self.z + other.z)/2)

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def norm(self):
        return math.sqrt(self.dot(self))

    def normalize(self):
        n = self.norm()
        return Vector(self.x / n, self.y / n, self.z / n) if n != 0 else self

    def scale(self, factor):
        return Vector(self.x * factor, self.y * factor, self.z * factor)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.direction = Vector(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)

    def intersection(self, other):
        # Assuming lines are in 2D for simplicity
        def det(a, b, c, d):
            return a * d - b * c
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = other.p1.x, other.p1.y
        x4, y4 = other.p2.x, other.p2.y
        denom = det(x1 - x2, y1 - y2, x3 - x4, y3 - y4)
        if denom == 0:
            return None
        x = det(det(x1, y1, x2, y2), x1 - x2, det(x3, y3, x4, y4), x3 - x4) / denom
        y = det(det(x1, y1, x2, y2), y1 - y2, det(x3, y3, x4, y4), y3 - y4) / denom
        return Point(x, y)

    def is_parallel(self, other):
        cross_dir = self.direction.cross(other.direction)
        return cross_dir.norm() == 0

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

class Polygon:
    def __init__(self, points):
        self.points = points

    def area(self):
        n = len(self.points)
        return 0.5 * abs(sum(self.points[i].x * self.points[(i + 1) % n].y - self.points[(i + 1) % n].x * self.points[i].y for i in range(n)))

    def convex_hull(self):
        points = sorted(self.points, key=lambda p: (p.x, p.y))
        if len(points) <= 1:
            return points

        def cross(o, a, b):
            return (a.x - o.x)*(b.y - o.y) - (a.y - o.y)*(b.x - o.x)

        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

    def contains_point(self, point):
        # Ray casting algorithm for point in polygon
        n = len(self.points)
        inside = False
        x, y = point.x, point.y
        for i in range(n):
            j = (i + 1) % n
            xi, yi = self.points[i].x, self.points[i].y
            xj, yj = self.points[j].x, self.points[j].y
            intersect = ((yi > y) != (yj > y)) and \
                        (x < (xj - xi) * (y - yi) / (yj - yi + 1e-10) + xi)
            if intersect:
                inside = not inside
        return inside

    def __repr__(self):
        return f"Polygon({self.points})"

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def contains_point(self, point):
        return self.center.distance_to(point) <= self.radius

    def intersect_line(self, line):
        # Assuming 2D for simplicity
        # Line in parametric form: P = p1 + t*(p2 - p1)
        dx = line.p2.x - line.p1.x
        dy = line.p2.y - line.p1.y
        fx = line.p1.x - self.center.x
        fy = line.p1.y - self.center.y

        a = dx**2 + dy**2
        b = 2 * (fx * dx + fy * dy)
        c = fx**2 + fy**2 - self.radius**2

        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return []  # No intersection
        discriminant = math.sqrt(discriminant)
        t1 = (-b - discriminant) / (2 * a)
        t2 = (-b + discriminant) / (2 * a)
        intersections = []
        if 0 <= t1 <= 1:
            intersections.append(Point(line.p1.x + t1 * dx, line.p1.y + t1 * dy))
        if 0 <= t2 <= 1:
            intersections.append(Point(line.p1.x + t2 * dx, line.p1.y + t2 * dy))
        return intersections

    def __repr__(self):
        return f"Circle({self.center}, {self.radius})"

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.width = abs(p2.x - p1.x)
        self.height = abs(p2.y - p1.y)
        self.points = [
            p1,
            Point(p2.x, p1.y),
            p2,
            Point(p1.x, p2.y)
        ]

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def contains_point(self, point):
        return min(self.p1.x, self.p2.x) <= point.x <= max(self.p1.x, self.p2.x) and \
               min(self.p1.y, self.p2.y) <= point.y <= max(self.p1.y, self.p2.y)

    def __repr__(self):
        return f"Rectangle({self.p1}, {self.p2})"

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        return 0.5 * abs((self.p1.x*(self.p2.y - self.p3.y) +
                          self.p2.x*(self.p3.y - self.p1.y) +
                          self.p3.x*(self.p1.y - self.p2.y)))

    def is_colinear(self):
        return self.area() == 0

    def centroid(self):
        return Point(
            (self.p1.x + self.p2.x + self.p3.x) / 3,
            (self.p1.y + self.p2.y + self.p3.y) / 3,
            (self.p1.z + self.p2.z + self.p3.z) / 3
        )

    def __repr__(self):
        return f"Triangle({self.p1}, {self.p2}, {self.p3})"

class Transformation:
    @staticmethod
    def rotate_point(point, angle, axis='z', origin=None):
        angle = math.radians(angle)
        x, y, z = point.x, point.y, point.z
        origin = origin or Point(0, 0, 0)
        x0, y0, z0 = origin.x, origin.y, origin.z
        if axis == 'z':
            xr = x0 + math.cos(angle) * (x - x0) - math.sin(angle) * (y - y0)
            yr = y0 + math.sin(angle) * (x - x0) + math.cos(angle) * (y - y0)
            zr = z
        elif axis == 'y':
            xr = x0 + math.cos(angle) * (x - x0) + math.sin(angle) * (z - z0)
            yr = y
            zr = z0 - math.sin(angle) * (x - x0) + math.cos(angle) * (z - z0)
        elif axis == 'x':
            xr = x
            yr = y0 + math.cos(angle) * (y - y0) - math.sin(angle) * (z - z0)
            zr = z0 + math.sin(angle) * (y - y0) + math.cos(angle) * (z - z0)
        return Point(xr, yr, zr)

    @staticmethod
    def scale_point(point, factor, origin=None):
        origin = origin or Point(0, 0, 0)
        return Point(
            origin.x + factor * (point.x - origin.x),
            origin.y + factor * (point.y - origin.y),
            origin.z + factor * (point.z - origin.z)
        )

    @staticmethod
    def reflect_point(point, axis_vector):
        dot_prod = Vector(point.x, point.y, point.z).dot(axis_vector)
        return Point(
            2 * dot_prod * axis_vector.x - point.x,
            2 * dot_prod * axis_vector.y - point.y,
            2 * dot_prod * axis_vector.z - point.z
        )
