


class Declaration:
    def __init__(self, ident, value):
        self.ident = ident
        self.value = value
    
    def evaluate(self, binding):
        return self.ident.evaluate(binding)

#######
# OPS #
#######

class Times:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def evaluate(self, binding):
        res = self.lhs.evaluate(binding) * self.rhs.evaluate(binding)
        return res
    
class Divide:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    def evaluate(self, binding):
        res = self.lhs.evaluate(binding) / self.rhs.evaluate(binding)
    
class Plus:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
        
    def evaluate(self, binding):
        res = self.lhs.evaluate(binding) + self.rhs.evaluate(binding)
        return res
    
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
