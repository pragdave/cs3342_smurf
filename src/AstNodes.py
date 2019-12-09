import math
from dataclasses import dataclass
from typing import List

#This file contains all the defintions for the AST Nodes
def binop_list(children):
    child = children[0]
    length = len(children)
    offset = 1
    while offset < length:
        op = children[offset]
        right = children[offset + 1]
        child = BinOpNode(child, op, right)
        offset += 2
    return child  


class CodeNode():
    def __init__(self, expr):
        self.expressions = expr

    def accept(self, visitor):
        return visitor.evaluate_code(self)


class VariableDeclarationNode():
    def __init__(self, vars):
        self.vars = vars

    def accept(self, visitor):
        return visitor.evaluate_variable_declaration(self)  


class DeclarationNode():
    def __init__(self, name, expr):
        self.name = name
        self.expression = expr

    def accept(self, visitor):
        return visitor.evaluate_declaration(self)  


class SimpleDeclarationNode():
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.evaluate_simple_declaration(self)   


class VariableReferenceNode():
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        return visitor.evaluate_variable_reference(self)


class IfNode():
    def __init__(self, condition, then):
        self.cond = condition
        self.then_branch = then

    def accept(self, visitor):
        return visitor.evaluate_if(self)


class IfElseNode():
    def __init__(self, condition, then, other):
        self.cond = condition
        self.then_branch = then
        self.else_branch = other

    def accept(self, visitor):
        return visitor.evaluate_ifelse(self)


class AssignmentNode():
    def __init__(self, name, expr):
        self.name = name
        self.expression = expr

    def accept(self, visitor):
        return visitor.evaluate_assignment(self)


class RelOpNode():
    rel_ops = {
        "==": lambda l, r: l == r,
        "!=": lambda l, r: l != r,
        ">=": lambda l, r: l >= r,
        ">": lambda l, r: l > r,
        "<=": lambda l, r: l <= r,
        "<": lambda l, r: l < r
    }

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.evaluate_rel_op(self)


class BinOpNode():
    bin_ops = {
        "+": lambda l, r: l + r,
        "-": lambda l, r: l - r,
        "*": lambda l, r: l * r,
        "/": lambda l, r: math.trunc(l/r)
    }

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.evaluate_bin_op(self)


class IntegerNode():
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_integer(self)

        
class FunctionCallNode():
    def __init__(self, name, args = []):
        self.name = name
        if type(args) != list:
            self.args = [args]
        else:
            self.args= args

    def accept(self, visitor):
        return visitor.evaluate_function_call(self)


class PrintFunctionNode():
    def __init__(self, listOfLists):
        self.listOfLists = listOfLists

    def accept(self, visitor):
        return visitor.evaluate_print_function(self)


class FunctionDefinitionNode():
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def accept(self, visitor):
        return visitor.evaluate_function_definition(self)  


class ThunkNode():
    def __init__(self, params, body, binding):
        self.formal_params = params
        self.body = body
        self.defining_binding = binding

    def accept(self, visitor, args):
        return visitor.evaluate_thunk(self, args)      
