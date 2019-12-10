# Binding
class Binding:
    def __init__(self):
        self.bindings = {}
    
    def set_variable(self, name, value):
        print(f"{name} -> {value}")
        self.bindings[name] = value
    
    def get_variable(self, name):
        return self.bindings.get(name, 0)

# Node Interpreter
class Assignment:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    
    def evaluate(self, binding):
        value = self.expr.evaluate(binding)
        binding.set_variable(self.name, value)
        return value

class VariableReference:
    def _init_(self, name):
        self.name = name
    
    def evaluate(self, binding):
        return binding.get_variable(self.name)

class IntegerNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self, binding):
        return self.value

# Arithemetic Operation
class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return (self.left.evaluate() + self.right.evaluate())

class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return (self.left.evaluate() - self.right.evaluate())

class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return (self.left.evaluate() * self.right.evaluate())

class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, binding):
        return int(self.left.evaluate() / self.right.evaluate())
    
