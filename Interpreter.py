class IntegerNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

# Arithemetic Operation
class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return (self.left.evaluate() + self.right.evaluate())

class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return (self.left.evaluate() - self.right.evaluate())

class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return (self.left.evaluate() * self.right.evaluate())

class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self):
        return int(self.left.evaluate() / self.right.evaluate())
    
