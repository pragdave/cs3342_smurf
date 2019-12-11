from dataclasses import dataclass
@dataclass
class Code:
    statements: []

    def eval(self, visitor):
        return visitor.interpret_code(self)
    
#####################
# Terminals
#####################

@dataclass
class Variable:
    name: str

    def eval(self, visitor):
        return visitor.interpret_variable(self)

@dataclass
class Integer:
    value: int

    def eval(self, visitor):
        return visitor.interpret_integer(self)
    
###########################
# Terminal Operations
###########################
@dataclass
class BinOp:
    left: None
    op: None
    right: None
    binary_operators = {
        "+": lambda l, r: l + r,
        "-": lambda l, r: l - r,
        "*": lambda l, r: l * r,
        "/": lambda l, r: l // r
    }


    def eval(self, visitor):
        
        return visitor.interpret_binop(self)
@dataclass
class RelOp:
    left: None
    op:   None
    right:None
    comparison_operators = {
        "==": lambda l, r: l == r,
        "!=": lambda l, r: l != r,
        ">=": lambda l, r: l >= r,
        ">" : lambda l, r: l >  r,
        "<=": lambda l, r: l <= r,
        "<" : lambda l, r: l < r
    }

    def eval(self, visitor):
        return visitor.interpret_relop(self)

###########################
# Structures
###########################

@dataclass
class Assignment:
    name: str
    expr: None

    def eval(self, visitor):
        return visitor.interpret_assignment(self)

@dataclass
class Decl:
    name: str
    expr: None
    def eval(self, visitor):
        return visitor.interpret_decl(self)

@dataclass
class VariableDecl:
    decls: None

    def eval(self, visitor):
        value = None
        for decl in self.decls:
            value = decl.eval(visitor)
        return value
    
@dataclass
class FunctionDef:
    params: None
    body: None

    def eval(self, visitor):
        return visitor.interpret_function_def(self)
    
@dataclass
class IfExpr:
    expr: None
    then_block: None
    else_block: None

    def eval(self, visitor):
        return visitor.interpret_if_expr(self)

@dataclass
class Thunk:
    params: None
    body: None
    binding: None

    def eval(self, visitor, args):
        return visitor.interpret_thunk(self, args)
    
class FunctionCall:
    def __init__(self, name, args = []):
        self.name = name
        self.args = list(args)
        
    def eval(self, visitor):
        return visitor.interpret_function_call(self)
    
class Print:
    def __init__(self,args = []):
        self.args = args[0]

    def eval(self, visitor):
        return visitor.interpret_print_call(self)