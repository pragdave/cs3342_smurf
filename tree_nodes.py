class Binding:
    def __init__(self):
        self.bindings = {}
    def set_variable(self, name, value):
        print(f"Set {name} to {value}")
        self.bindings[name] = value
    def get_variable_value(self, name):
        return self.bindings.get(name, 0)

class Variable:
    def __init__(self, name):
        self.name = name
    def evaluate(self, binding):
        return binding.get_variable_value(self.name)


class Code:
    def __init__(self, expressions):
        self.expressions = expressions

    def run(self, binding):
        value = 0
        for exp in self.expressions:
            value = e.run(binding)
        return value

class Assignment:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
    def run(self, binding):
        value = self.expression.run(binding)
        binding.set_variable(self.name, value)
        return value
        

class Print:
    def __init__(self, value):
        self.value = value
    def run(self, binding):
        print(value)

#######
# OPS #
#######

class Times:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        left = self.lhs.evaluate(binding)
        right = self.rhs.evaluate(binding)
        return left*right
    
class Divide:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    def evaluate(self, binding):
        left = self.lhs.evaluate(binding)
        right = self.rhs.evaluate(binding)
        return left / right
    
class Plus:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    def evaluate(self, binding):
        left = self.lhs.evaluate(binding)
        right = self.rhs.evaluate(binding)
        return left+right
    
class Minus:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        res = self.lhs.evaluate(binding) - self.rhs.evaluate(binding)
        return res
    
class Equals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        if(self.lhs.evaluate(binding) == self.rhs.evaluate(binding)):
            return True
        return False

class NotEquals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        if(self.lhs.evaluate(binding) == self.rhs.evaluate(binding)):
            return False
        return True

class GreaterEquals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        if(self.lhs.evaluate(binding) >= self.rhs.evaluate(binding)):
            return True
        return False
    
class Greater:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        if(self.lhs.evaluate(binding) > self.rhs.evaluate(binding)):
            return True
        return False
    
class LessEquals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        if(self.lhs.evaluate(binding) <= self.rhs.evaluate(binding)):
            return True
        return False

class Less:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        if(self.lhs.evaluate(binding) < self.rhs.evaluate(binding)):
            return True
        return False

#############
# TERMINALS #
#############

class Integer:
    def __init__(self, value):
        self.value = value
    
    def evaluate(self, binding):
        return self.value

class Identifier:
    def __init__(self, ident):
        self.ident = ident
    
    def evaluate(self, binding):
        return self.ident.evaluate(binding)
