# class BinopNode:
#     def __init__(self, left, verb, right):
#         self.left = left
#         self.verb = verb
#         self.right = right

#     def __str__(self):
#         return f"{self.verb} {self.left} {self.right}"

class IntegerNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def __str__(self):
        return str(self.value)

# Arithemetic Operation
class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return self.left.evaluate(binding) + self.right.evaluate(binding)

class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return self.left.evaluate(binding) - self.right.evaluate(binding)

class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return self.left.evaluate(binding) * self.right.evaluate(binding)

class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return self.left.evaluate(binding) / self.right.evaluate(binding)
    
