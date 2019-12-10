class IntegerNode:
    def __init__(self, value):
        self.value = value

    def accept(self):
        return self.value

# Arithemetic Operation
class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self):
        return (self.left.accept() + self.right.accept())

class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self):
        return (self.left.accept() - self.right.accept())

class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self):
        return (self.left.accept() * self.right.accept())

class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self):
        return int(self.left.accept() / self.right.accept())
    
