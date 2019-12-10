import bindings as binding

class Variable:
    def __init__(self, name):
        self.name = name
    
    def accept(self, visitor, binding):
        return visitor.evaluate_var_value(self, binding)


class Code:
    def __init__(self, expressions):
        self.expressions = expressions
    
    def accept(self, visitor, binding):
        return visitor.evaluate_code(self, binding)

class Assignment:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
    
    def accept(self, visitor, binding):
        return visitor.evaluate_assignment(self, binding)


#######
# OPS #
#######

class Times:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_times(self, binding)
    
class Divide:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_divide(self, binding)
    
class Plus:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_plus(self, binding)
    
class Minus:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_minus(self, binding)

class Equals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_equals(self, binding)
        

class NotEquals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_not_equals(self, binding)

class GreaterEquals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_greater_equal(self, binding)
    
class Greater:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_greater_than(self, binding)
    
class LessEquals:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_less_equal(self, binding)

class Less:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_less_than(self, binding)

#############
# TERMINALS #
#############

class Integer:
    def __init__(self, value):
        self.value = value
    
    def accept(self, visitor, binding):
        return visitor.evaluate_integer(self, binding)

class Identifier:
    def __init__(self, ident):
        self.ident = ident
    
    def accept(self, visitor, binding):
        return visitor.evaluate_identifier(self, binding)
