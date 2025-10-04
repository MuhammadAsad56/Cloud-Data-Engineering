# Q1 


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())



# Q2  

class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self, current_year):
        return current_year - self.birth_year

p = Person("Asad", "Pakistan", 2000)
print("Name:", p.name)
print("Country:", p.country)
print("Age:", p.age(2025))



# Q 3

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))

