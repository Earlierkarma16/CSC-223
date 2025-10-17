import abc
import math

# Step 1: Define an Abstract Base Class
class BasicShape(abc.ABC):
    def __init__(self, name: str):
        self._area = 0.0
        self._name = name

    # Property for _area
    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self, value: float):
        if value >= 0:
            self._area = value
        else:
            raise ValueError("Area cannot be negative.")

    # Property for _name
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @abc.abstractmethod
    def calc_area(self):
        pass

# Step 2: Define a Derived Class Circle
class Circle(BasicShape):
    def __init__(self, x: float, y: float, r: float, n: str = "Circle"):
        super().__init__(n)
        self._x_center = x
        self._y_center = y
        self._radius = r
        self.calc_area()

    @property
    def x_center(self) -> float:
        return self._x_center

    @property
    def y_center(self) -> float:
        return self._y_center

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, r: float):
        if r >= 0:
            self._radius = r
            self.calc_area()
        else:
            raise ValueError("Radius cannot be negative.")

    def calc_area(self):
        self.area = math.pi * (self._radius ** 2)

# Step 3: Define a Derived Class Rectangle
class Rectangle(BasicShape):
    def __init__(self, l: float, w: float, n: str = "Rectangle"):
        super().__init__(n)
        self._length = l
        self._width = w
        self.calc_area()

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, l: float):
        if l >= 0:
            self._length = l
            self.calc_area()
        else:
            raise ValueError("Length cannot be negative.")

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, w: float):
        if w >= 0:
            self._width = w
            self.calc_area()
        else:
            raise ValueError("Width cannot be negative.")

    def calc_area(self):
        self.area = self._length * self._width

# Step 4: Define a Derived Class Square
class Square(Rectangle):
    def __init__(self, s: float, n: str = "Square"):
        super().__init__(s, s, n)
        self._side = s
        self.name = n # Re-set the name to "Square"

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, s: float):
        if s >= 0:
            self._side = s
            self.length = s
            self.width = s
        else:
            raise ValueError("Side cannot be negative.")

# Step 5: Create a Test Program
if __name__ == '__main__':
    # 1. Create a list called shapes
    shapes = []

    # 2. Add shape objects
    shapes.append(Rectangle(l=10.0, w=20.0, n="Rectangle_1"))
    shapes.append(Rectangle(l=20.0, w=30.0, n="Rectangle_2"))
    shapes.append(Circle(x=0.0, y=0.0, r=4.0, n="Circle_1"))
    shapes.append(Circle(x=1.0, y=2.0, r=9.0, n="Circle_2"))
    shapes.append(Square(s=10.0, n="Square"))

    # 3. Loop through the shapes list and display info
    print("--- Polymorphism check ---")
    for shape in shapes:
        # Dynamic method resolution calls the correct getter and area
        print(f"{shape.name} Area = {shape.area:.5f}")

    # 4. Use Circle from list for getter/setter check
    print("\n--- Getter/setter check ---")
    circle_to_test = shapes[2]
    print(f"{circle_to_test.name} Current: {circle_to_test.radius} {circle_to_test.area:.5f}")
    circle_to_test.radius = 8.0
    print(f"{circle_to_test.name} Doubled: {circle_to_test.radius} {circle_to_test.area:.5f}")

    # 5. Use Rectangle from list for getter/setter check
    rectangle_to_test = shapes[0]
    print(f"{rectangle_to_test.name} Current: {rectangle_to_test.length} {rectangle_to_test.width} {rectangle_to_test.area:.5f}")
    rectangle_to_test.length = 20.0
    rectangle_to_test.width = 40.0
    print(f"{rectangle_to_test.name} Doubled: {rectangle_to_test.length} {rectangle_to_test.width} {rectangle_to_test.area:.5f}")

    # 6. Use Square from list for getter/setter check
    square_to_test = shapes[4]
    print(f"{square_to_test.name} Current: {square_to_test.side} {square_to_test.area:.5f}")
    square_to_test.side = 20.0
    print(f"{square_to_test.name} Doubled: {square_to_test.side} {square_to_test.area:.5f}")

