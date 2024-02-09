#1
class StringManipulator:
    def __init__(self):
        self.input_string = ""
    def getString(self):
        self.input_string = input("Enter a string: ")
    def printString(self):
        print("String in upper case:", self.input_string.upper())
manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

#2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length
#примеры:
shape = Shape()
print("Area of Shape:", shape.area())
square = Square(5)
print("Area of Square:", square.area())

#3
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rectangle = Rectangle(4, 6)
print("Area of Rectangle:", rectangle.area())

#4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance
point1 = Point(3, 4)
point2 = Point(6, 8)
point1.show()
point2.show()
distance = point1.dist(point2)
print("Distance between the points:", distance)
point1.move(5, 7)
point1.show()

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted.")
        else:
            print("Deposit amount must be greater than zero.")
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")
account = Account("John Doe", 1000)
print("Initial balance:", account.balance)
account.deposit(500)
print("Balance after deposit:", account.balance)
account.withdraw(200)
print("Balance after withdrawal:", account.balance)
account.withdraw(2000)
print("Balance after attempted overdraw:", account.balance)

#6
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)