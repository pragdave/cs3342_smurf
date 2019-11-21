import math
from dataclasses import dataclass
from typing import List


def binop_list(children):
    child = children[0]
    length = len(children)
    offset = 1
    while offset < length:
        op = children[offset]
        right = children[offset + 1]
        child = BinOp(child, op, right)
        offset += 2
    return child    

def relop_list(children):
    child = children[0]
    length = len(children)
    offset = 1
    while offset < length:
        op = children[offset]
        right = children[offset + 1]
        child = RelOp(child, op, right)
        offset += 2
    return child    



@dataclass
class Code():
    expressions: List['Expr']

    def accept(self, visitor):
        return visitor.evaluate_code(self)
    
@dataclass
class Integer():
    value: int

    def accept(self, visitor):
        return visitor.evaluate_integer(self)
        
@dataclass
class If():
    cond: 'Expr'
    then_branch: 'Expr'

    def accept(self, visitor):
        return visitor.evaluate_if(self)

@dataclass
class IfElse():
    cond:        'Expr'
    then_branch: 'Expr'
    else_branch: 'Expr'

    def accept(self, visitor):
        return visitor.evaluate_ifelse(self)

@dataclass
class Expr():
    expression: 'Expr'

    def accept(self, visitor):
        return visitor.evaluate_expr(self)


@dataclass
class BinOp():
    left: 'Expr'
    op: str
    right:  'Expr'

    def accept(self, visitor):
        return visitor.evaluate_bin_op(self)

@dataclass
class RelOp():
    left: 'Expr'
    op: str
    right: 'Expr'

    def accept(self, visitor):
        return visitor.evaluate_rel_op(self)

@dataclass
class VariableReference():
    name: str

    def accept(self, visitor):
        return visitor.evaluate_variable_reference(self)

class Declaration():
    def __init__(self, name, expr):
        self.name = name
        self.expression = expr

    def accept(self, visitor):
        return visitor.evaluate_declaration(self)

class SimpleDeclaration():
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.evaluate_simple_declaration(self)

@dataclass
class Assignment():
    name: str
    expression: 'Expr'

    def accept(self, visitor):
        return visitor.evaluate_assignment(self)

@dataclass
class FunctionDecl():
    params: List[str]
    body: 'Code'

    def accept(self, visitor):
        return visitor.evaluate_function_decl(self)

class FunctionCall():
    def __init__(self, name, args = []):
        self.name = name
        if type(args) != list:
            self.args = [args]
        else:
            self.args= args

    def accept(self, visitor):
        return visitor.evaluate_function_call(self)

class PrintFunc():
    def __init__(self, listOfLists):
        self.listOfLists = listOfLists

    def accept(self, visitor):
        return visitor.evaluate_print_func(self)

class Thunk():
    def __init__(self, params, body, binding):
        self.formal_params = params
        self.body = body
        self.defining_binding = binding

    def accept(self, visitor, args):
        return visitor.evaluate_thunk(self, args)

class VariableDeclaration():
    def __init__(self, vars):
        self.vars = vars

    def accept(self, visitor):
        return visitor.evaluate_variable_declaration(self)

