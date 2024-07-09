class Rectangle:
    """
    Метод __add__ объединяет два прямоугольника по периметру и создает новый прямоугольник.
    Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров исходных прямоугольников, и создает новый прямоугольник.
    Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
    Методы __str__ и __repr__ предоставляют строковое представление объекта класса Rectangle.
    """
    def __init__(self, width: int, height: int=None) -> None:
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height
            
    def perimeter(self):
        return 2 * (self.height + self.width)
    
    def area(self):
        return self.width * self.height
        
    
    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        new_rectangle = Rectangle(new_width, new_height)
        return new_rectangle
    
    def __sub__(self, other):
        perimeter_self = self.perimeter()
        perimeter_other = other.perimeter()
        new_perimeter = abs(perimeter_self - perimeter_other)
        
        new_width = new_perimeter // self.width
        new_height = (new_perimeter - (2 * new_width)) / 2
        
        new_rectangle = Rectangle(int(new_width), int(new_height))
        return new_rectangle
    
    def __lt__(self, other):
        self_area = self.area()
        other_area = other.area()
        if(self_area < other_area):
            return True
        else:
            return False
        
    def __eq__(self, other):
        self_area = self.area()
        other_area = other.area()
        if(self_area == other_area):
            return True
        else:
            return False
        
    def __le__(self, other):
        self_area = self.area()
        other_area = other.area()
        if(self_area <= other_area):
            return True
        else:
            return False
    
    def __str__(self) -> str:
        return f'Прямоугольник со сторонами {self.width} и {self.height}'
    
    def __repr__(self) -> str:
        return f'Rectangle({self.width}, {self.height})'
    
    
if __name__ == '__main__':
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())

    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    print(rect_sum)
    print(rect_diff)

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))      
