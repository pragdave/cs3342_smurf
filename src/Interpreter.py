import math
from typing import List
from AstNodes import *

class Binding:
    def __init__(self, outer=None):
        self.bindings = {}
        self.outer = outer

    def push(self):
        return Binding(self)
    
    def pop(self):
        return self.outer

    def set_variable(self, name, value):
        self.bindings[name] = value

    def get_variable_value(self, name):
        if name in self.bindings:
            return self.bindings[name]

        if self.outer:
            return self.outer.get_variable_value(name)

        raise Exception(f"Variable '{name}' is not defined")


#Interpreter class for Smurf
class Interpreter:
    def __init__(self):
        self.binding = Binding()

    def evaluate_code(self, node):
        value = 0
        for e in node.expressions:
            value = e.accept(self)
        return value

    def evaluate_variable_declaration(self, node):
        value = 0
        for var in node.vars:
            value = var.accept(self)
        return value

    def evaluate_declaration(self, node):
        self.binding.set_variable(node.name, node.expression.accept(self))

    def evaluate_simple_declaration(self, node):
        self.binding.set_variable(node.name, None)

    def evaluate_variable_reference(self, node):
        return self.binding.get_variable_value(node.name)

    def evaluate_if(self, node):
        if node.cond.accept(self) != 0:
            return node.then_branch.accept(self)

    def evaluate_ifelse(self, node):
        if node.cond.accept(self) != 0:
            return node.then_branch.accept(self)
        else:
            return node.else_branch.accept(self)

    def evaluate_assignment(self, node):
        value = node.expression.accept(self)
        self.binding.set_variable(node.name, value)
        return value

    def evaluate_rel_op(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        return node.rel_ops[node.op](left, right)

    def evaluate_bin_op(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        return node.bin_ops[node.op](left, right)

    def evaluate_integer(self, node):
        try:
            return node.value
        except ValueError:
            return self.binding.get_variable_value(node.value)

    def evaluate_function_call(self, node):
        arg_values = [
            arg.accept(self) for arg in node.args
        ]
        thunk = self.binding.get_variable_value(node.name)
        return thunk.accept(self, arg_values)

    def evaluate_print_function(self, node):
        lists = node.listOfLists[0]
        printLine = "Print: "
        for expr in lists:
            printLine += str(expr.accept(self))
            printLine += "|"
        printLine = printLine[:-1]
        print(printLine)
        return printLine

    def evaluate_function_definition(self, node):
        return ThunkNode(node.params, node.body, self.binding)

    def evaluate_thunk(self, node, args):       
        temp = self.binding
        self.binding = node.defining_binding
        self.binding = self.binding.push()
       
        for formal, actual in zip(node.formal_params, args):
            self.binding.set_variable(formal.name, actual)
        
        result = node.body.accept(self)
        
        self.binding = temp
        return result
