class Shape:
    def __init__(self, shape_id, *args):
        self.shape_id = shape_id
        self.vertices = list(args)

    def move(self, x_offset, y_offset):
        self.vertices = [(x + x_offset, y + y_offset) for x, y in self.vertices]

    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

class Triangle(Shape):
    def __init__(self, shape_id, vertex1, vertex2, vertex3):
        super().__init__(shape_id, vertex1, vertex2, vertex3)

    def area(self):
        (x1, y1), (x2, y2), (x3, y3) = self.vertices
        return abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2

class Pentagon(Shape):
    def __init__(self, shape_id, vertex1, vertex2, vertex3, vertex4, vertex5):
        super().__init__(shape_id, vertex1, vertex2, vertex3, vertex4, vertex5)

    def area(self):
        x, y = zip(*self.vertices)
        return 0.5 * abs(sum(x[i] * y[i+1] - x[i+1] * y[i] for i in range(-1, len(x)-1)))

def compare(shape1, shape2):
    area1 = shape1.area()
    area2 = shape2.area()
    if area1 > area2:
        return f"{shape1.shape_id} is larger than {shape2.shape_id}"
    elif area1 < area2:
        return f"{shape1.shape_id} is smaller than {shape2.shape_id}"
    else:
        return f"{shape1.shape_id} and {shape2.shape_id} are of equal size"

# Example usage
triangle = Triangle("Triangle1", (0, 0), (1, 0), (0, 1))
pentagon = Pentagon("Pentagon1", (0, 0), (1, 0), (1.5, 1), (1, 2), (0, 2))

print(compare(triangle, pentagon))
triangle.move(2, 3)
print(triangle.vertices) 	