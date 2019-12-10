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

class Arithmetic_Expression:
    def __init__(self, lhs, expressions):
        self.lhs = lhs
        self.expressions = expressions
        
    def accept(self, visitor, binding):
        return visitor.evaluate_arith_expr(self, binding)

class Mult_Term:
    def __init__(self, lhs, expressions):
        self.lhs = lhs
        self.expressions = expressions
    
    def accept(self, visitor, binding):
        return visitor.evaluate_mult_term(self, binding)
    
class Boolean_Expression:
    def __init__(self, lhs, op, rhs):
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
    
    def accept(self, visitor, binding):
        return visitor.evaluate_bool_expr(self, binding)
    
class Print_Smurf:
    def __init__(self, to_print):
        self.to_print = to_print
    
    def accept(self, visitor, binding):
        return visitor.evaluate_print_smurf(self, binding)

#############
# TERMINALS #
#############

class Integer:
    def __init__(self, sign, value):
        self.sign = sign
        self.value = value
    
    def accept(self, visitor, binding):
        return visitor.evaluate_integer(self, binding)

class Identifier:
    def __init__(self, ident):
        self.ident = ident
    
    def accept(self, visitor, binding):
        return visitor.evaluate_identifier(self, binding)
