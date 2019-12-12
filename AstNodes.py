#value: int
#sign: -/none
class Number:
    def __init__(self, value, sign):
        self.value = value
        self.sign = sign
	
    def accept(self, visitor, bindings):
        return visitor.evaluate_number(self, bindings)

#ident: identifier (string)
class Var_Ref:
    def __init__(self, ident):
        self.ident = ident
	
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_ref(self, bindings)

#value: evaluated smallest component (int)
class Factor:
    def __init__(self, value):
        self.value = value
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_factor(self, bindings)

#factor: LHS of * or /
#multAndFactList: Zero or more( (* or /), factor)
class Mult_Term:
    def __init__(self, factor, multAndFactList):
        self.factor = factor
        self.multAndFactList = multAndFactList
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_mult_term(self, bindings)

#multTerm: LHS of + or -
#plusAndTermList: Zero or more( (+ or -), multTerm)
class Arithmetic_Expression:
    def __init__(self, multTerm, plusAndTermList):
        self.multTerm = multTerm
        self.plusAndTermList = plusAndTermList
    
    def accept(self, visitor, bindings):
        return visitor.evaluate_arithmetic_expression(self, bindings)

#name: var_ref
#expr: RHS of equals
class Var_Decl:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_decl(self, bindings)

#list: a list of var_decl
class Var_Let:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_var_let(self, bindings)

#left: evaluatable LHS of operator
#op: bool op: ==, !=, >=, >, <=, < 
#right: evaluatable RHS of operator
class Boolean_Expression:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_boolean_expression(self, bindings)

#listOfList: A list where 0 element is a list of all print inputs separated by comma
class Print_Func:
    def __init__(self, listOfList):
        self.listOfList = listOfList
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_print_func(self, bindings)

#list: list of expression
class Code_Block:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor, bindings, fn_decl=False):
        return visitor.evaluate_code_block(self, bindings, fn_decl)

#boolExpr: boolean_expression
#ifBlock: code_block ran if boolExpr is true
#elseBlock: code_block ran if boolExpr is false
class If_Statement:
    def __init__(self, boolExpr, ifBlock, elseBlock):
        self.boolExpr = boolExpr
        self.ifBlock = ifBlock
        self.elseBlock = elseBlock
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_if_statement(self, bindings)

#name: identifier
#paramList: list of parameter names used in function
#codeBlock: the code executed by the function
class Fn_Decl:
    def __init__(self, name, paramList, codeBlock):
        self.name = name
        self.paramList = paramList
        self.codeBlock = codeBlock
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_fn_decl(self, bindings)

#list: list of fn_decl
class Fn_Let:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_fn_let(self, bindings)

#name: identifier
#paramList: values passed into the function
class Fn_Call:
    def __init__(self, name, paramList):
        self.name = name
        self.paramList = paramList
        
    def accept(self, visitor, bindings):
        return visitor.evaluate_fn_call(self, bindings)

#list: list of valid lines
class Code:
    def __init__(self, list):
        self.list = list
        
    def accept(self, visitor):
        return visitor.evaluate_code(self)