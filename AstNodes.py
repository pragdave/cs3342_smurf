class Number:
    def __init__(self, value):
        self.value = value
	
    def accept(self, visitor):
        return visitor.evaluate_number(self)
        
class Factor:
    def __init__(self, value, sign):
        self.value = value
        self.sign = sign
    
    def accept(self, visitor):
        return visitor.evaluate_factor(self)

class Term:
    def __init__(self, factor, multAndFactList):
        self.factor = factor
        self.multAndFactList = multAndFactList
        
    def accept(self, visitor):
        return visitor.evaluate_term(self)

class Arithmetic_Expression:
    def __init__(self, term, plusAndTermList):
        self.term = term
        self.plusAndTermList = plusAndTermList
    
    def accept(self, visitor):
        return visitor.evaluate_arithmetic_expression(self)

class Boolean_Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
    def accept(self, visitor):
        return visitor.evaluate_boolean_expression(self)

class Print:
    def __init__(self, expression, list):
        self.expression = expression
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_print(self)

class Code:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_code(self)