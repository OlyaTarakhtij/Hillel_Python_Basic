import math

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return math.isclose(self.get_square(), other.get_square(), rel_tol=1e-9, abs_tol=1e-12)

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        new_width = self.width
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        if n <= 0:
            raise ValueError("Multiplier must be positive")
        return Rectangle(self.width, self.height * n)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __str__(self):
        area = self.get_square()
        w = int(self.width) if math.isclose(self.width, round(self.width)) else self.width
        h = int(self.height) if math.isclose(self.height, round(self.height)) else self.height
        a = int(area) if math.isclose(area, round(area)) else area
        return f"Rectangle(width={w}, height={h}, area={a})"
