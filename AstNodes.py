class Number:
    def __init__(self, value, sign):
        self.value = value
        self.sign = sign
	
    def accept(self, visitor, bindings):
        return visitor.evaluate_number(self, bindings)
        
class Var_Ref:
    def __init__(self, ident):
        self.ident = ident
	
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_ref(self, bindings)
        
class Factor:
    def __init__(self, value):
        self.value = value
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_factor(self, bindings)

class Mult_Term:
    def __init__(self, factor, multAndFactList):
        self.factor = factor
        self.multAndFactList = multAndFactList
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_mult_term(self, bindings)

class Arithmetic_Expression:
    def __init__(self, multTerm, plusAndTermList):
        self.multTerm = multTerm
        self.plusAndTermList = plusAndTermList
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_arithmetic_expression(self, bindings)

class Var_Decl:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_decl(self, bindings)
    
class Var_Let:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_let(self, bindings)

class Boolean_Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_boolean_expression(self, bindings)

class Print_Func:
    def __init__(self, listOfList):
        self.listOfList = listOfList
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_print_func(self, bindings)
        
class Code_Block:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor, bindings, fn_decl=False):
        return visitor.evaluate_code_block(self, bindings, fn_decl)
        
class If_Statement:
    def __init__(self, boolExpr, ifBlock, elseBlock):
        self.boolExpr = boolExpr
        self.ifBlock = ifBlock
        self.elseBlock = elseBlock
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_if_statement(self, bindings)
        
class Fn_Decl:
    def __init__(self, name, paramList, codeBlock):
        self.name = name
        self.paramList = paramList
        self.codeBlock = codeBlock
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_fn_decl(self, bindings)
        
class Fn_Let:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_fn_let(self, bindings)
        
class Fn_Call:
    def __init__(self, name, paramList):
        self.name = name
        self.paramList = paramList
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_fn_call(self, bindings)
        
class Code:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_code(self)