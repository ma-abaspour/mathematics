
class Tensor:
    def __init__(self, data):
        self.data = data
        self.shape = self.compute_shape(data)

    @staticmethod
    def compute_shape(data):
        """Recursively compute the shape of the tensor."""
        if isinstance(data, list):
            return [len(data)] + Tensor.compute_shape(data[0]) if data else []
        return []

    def __add__(self, other):
        """Element-wise addition of two tensors."""
        if self.shape != other.shape:
            raise ValueError("Tensors must have the same shape for addition.")
        return Tensor([
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __sub__(self, other):
        """Element-wise subtraction of two tensors."""
        if self.shape != other.shape:
            raise ValueError("Tensors must have the same shape for subtraction.")
        return Tensor([
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ])

    def __mul__(self, scalar):
        """Element-wise scalar multiplication."""
        return Tensor([[x * scalar for x in row] for row in self.data])

    def __truediv__(self, scalar):
        """Element-wise scalar division."""
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Tensor([[x / scalar for x in row] for row in self.data])

    def dot(self, other):
        """Dot product for 2D tensors (matrix multiplication)."""
        if len(self.shape) != 2 or len(other.shape) != 2:
            raise ValueError("Dot product is only defined for 2D tensors.")
        if self.shape[1] != other.shape[0]:
            raise ValueError("Inner dimensions must match for dot product.")
        return Tensor([
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.shape[1]))
             for j in range(other.shape[1])]
            for i in range(self.shape[0])
        ])

    def transpose(self):
        """Transpose a 2D tensor."""
        if len(self.shape) != 2:
            raise ValueError("Transpose is only defined for 2D tensors.")
        return Tensor([[self.data[j][i] for j in range(self.shape[0])] for i in range(self.shape[1])])

    def contract(self):
        """Sum all elements of the tensor."""
        def recursive_sum(data):
            if isinstance(data, list):
                return sum(recursive_sum(d) for d in data)
            return data
        return recursive_sum(self.data)

    def reshape(self, new_shape):
        """Reshape a tensor while preserving its data."""
        if self.contract() != sum(sum(row) for row in self.data):  # Shape mismatch check
            raise ValueError("Cannot reshape tensor due to size mismatch.")
        flat_data = [x for row in self.data for x in row]
        reshaped_data = Tensor.build_reshaped(flat_data, new_shape)
        return Tensor(reshaped_data)

    @staticmethod
    def build_reshaped(flat_data, shape):
        """Helper to reshape flat data into a nested list."""
        if len(shape) == 1:
            return flat_data[:shape[0]]
        sub_shape = shape[1:]
        step = int(len(flat_data) / shape[0])
        return [Tensor.build_reshaped(flat_data[i * step:(i + 1) * step], sub_shape)
                for i in range(shape[0])]

    def __repr__(self):
        return f"Tensor({self.data})"


# T1 = Tensor([[1, 2], [3, 4]])
# T2 = Tensor([[5, 6], [7, 8]])
# T3 = Tensor([[1, 2, 3], [4, 5, 6]])

# print(T1 + T2)
# print(T1 - T2)
# print(T1 * 2)
# print(T1 / 2)
# print(T1.dot(T2.transpose()))
# print(T3.transpose())
# print(T1.contract())

# T4 = Tensor([[1, 2, 3, 4]])
# print("Reshape T4 to 2x2:")
# print(T4.reshape([2, 2]))
