import copy

class Shape:
    def __init__(self, color):
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def __str__(self):
        return f"Circle: radius={self.radius}, color={self.color}"

# Створюємо оригінальний об'єкт
original = Circle(10, "red")
print("Original:", original)

# Клонуємо його
copy_circle = original.clone()
print("Clone:", copy_circle)
