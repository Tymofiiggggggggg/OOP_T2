import copy
#Створюємо базовий клас Shape з конструктором, який приймає параметр color і зберігає його в атрибуті об'єкта
class Shape:
    def __init__(self, color):
        self.color = color   
    #Метод clone() створює повну (глибоку) копію об'єкта за допомогою copy.deepcopy()
    def clone(self):
        return copy.deepcopy(self)
    #Метод __str__() визначає, як об'єкт буде представлений у вигляді рядка при виведенні 
    def __str__(self):
        return f"{self.__class__.__name__}: {self.get_attributes()}, color={self.color}"
    #Допоміжний метод, який повертає порожній рядок. Підкласи (Circle, Rectangle) перевизначатимуть йог
    def get_attributes(self):
        return ""

class Circle(Shape):
    #Конструктор приймає radius і color, викликає конструктор батьківського класу (super().__init__) для ініціалізації кольору, і зберігає радіус
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    #Перевизначає метод get_attributes(), повертаючи рядок з радіусом кола
    def get_attributes(self):
        return f"radius={self.radius}"

original_circle = Circle(10, "red")
print("Original:", original_circle)
circle_clone = original_circle.clone()
print("Clone:", circle_clone)
