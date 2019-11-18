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

class Mult_Term:
    def __init__(self, factor, multAndFactList):
        self.factor = factor
        self.multAndFactList = multAndFactList
        
    def accept(self, visitor):
        return visitor.evaluate_mult_term(self)

class Arithmetic_Expression:
    def __init__(self, multTerm, plusAndTermList):
        self.multTerm = multTerm
        self.plusAndTermList = plusAndTermList
    
    def accept(self, visitor):
        return visitor.evaluate_arithmetic_expression(self)

class Var_Decl:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        
    def accept(self, visitor):
        return visitor.evaluate_var_decl(self)
    
class Let:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_let(self)

class Boolean_Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
    def accept(self, visitor):
        return visitor.evaluate_boolean_expression(self)

class Print_Func:
    def __init__(self, expression, list):
        self.expression = expression
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_print_func(self)
        
class Code_Block:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_code_block(self)
        
class If_Statement:
    def __init__(self, boolExpr, ifBlock, elseBlock):
        self.boolExpr = boolExpr
        self.ifBlock = ifBlock
        self.elseBlock = elseBlock
        
    def accept(self, visitor):
        return visitor.evaluate_if_statement(self)
        
class Code:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_code(self)