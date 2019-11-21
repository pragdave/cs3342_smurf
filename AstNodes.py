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



class Code():
    def __init__(self, expr):
        self.expressions = expr

    def accept(self, visitor):
        return visitor.evaluate_code(self)

class VariableDeclaration():
    def __init__(self, vars):
        self.vars = vars

    def accept(self, visitor):
        return visitor.evaluate_variable_declaration(self)  

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

class VariableReference():
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.evaluate_variable_reference(self)

class If():
    def __init__(self, condition, then):
        self.cond = condition
        self.then_branch = then

    def accept(self, visitor):
        return visitor.evaluate_if(self)

class IfElse():
    def __init__(self, condition, then, other):
        self.cond = condition
        self.then_branch = then
        self.else_branch = other

    def accept(self, visitor):
        return visitor.evaluate_ifelse(self)

class Assignment():
    def __init__(self, name, expr):
        self.name = name
        self.expression = expr

    def accept(self, visitor):
        return visitor.evaluate_assignment(self)

class RelOp():
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.evaluate_rel_op(self)

class BinOp():
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.evaluate_bin_op(self)

class Integer():
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_integer(self)
        
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

class FunctionDef():
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def accept(self, visitor):
        return visitor.evaluate_function_def(self)  

class Thunk():
    def __init__(self, params, body, binding):
        self.formal_params = params
        self.body = body
        self.defining_binding = binding

    def accept(self, visitor, args):
        return visitor.evaluate_thunk(self, args)      
