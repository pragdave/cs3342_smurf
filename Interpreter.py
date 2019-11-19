import math
from typing import List

bin_ops = {
    "+": lambda l, r: l + r,
    "-": lambda l, r: l - r,
    "*": lambda l, r: l * r,
    "/": lambda l, r: math.trunc(l/r)
}

rel_ops = {
    "==": lambda l, r: l == r,
    "!=": lambda l, r: l != r,
    ">=": lambda l, r: l >= r,
    ">": lambda l, r: l > r,
    "<=": lambda l, r: l <= r,
    "<": lambda l, r: l < r
}

class Binding:
    def __init__(self):
        self.bindings = [{}]

    def push(self):
        return self.bindings.append({})

    def pop(self):
        return self.bindings.pop()

    def set_variable(self, name, value):
        print(f"Set {name} to {value}")
        self.bindings[-1][name] = value

    def get_variable_value(self, name):
        for e in reversed(self.bindings):
            if name in e:
                return e[name]
            

        if self.bindings[-1]:
            return self.bindings[-1].get_variable_value(name)

        raise Exception(f"Variable '{name}' is not defined")  

class Interpreter:
    def __init__(self):
        self.varBinding = Binding()
        self.funcBinding = Binding()

    def evaluate_expr(self, node):
        return node.expression.accept(self)

    def evaluate_integer(self, node):
        try:
            return node.value
        except ValueError:
            return self.varBinding.get_variable_value(node.value)

    def evaluate_bin_op(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        return bin_ops[node.op](left, right)

    def evaluate_code(self, node):
        value = 0
        for e in node.expressions:
            value = e.accept(self)
        return value

    def evaluate_rel_op(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        return rel_ops[node.op](left, right)

    def evaluate_variable_reference(self, node):
        return self.varBinding.get_variable_value(node.name)

    def evaluate_declaration(self, node):
        self.varBinding.push()
        self.varBinding.set_variable(node.name, node.expression.accept(self))
        print("variable bindings: ", self.varBinding.bindings)

    def evaluate_simple_declaration(self, node):
        self.varBinding.push()
        self.varBinding.set_variable(node.name, None)
        print("variable bindings: ", self.varBinding.bindings)

    def evaluate_if(self, node):
        if node.cond.accept(self) != 0:
            return node.then_branch.accept(self)

    def evaluate_ifelse(self, node):
        if node.cond.accept(self) != 0:
            return node.then_branch.accept(self)
        else:
            return node.else_branch.accept(self)

    # def evaluate_assignment(self, node):
    #     value = node.expression.accept(self.binding)
    #     self.binding.set_variable(node.name, value)
    #     return value

    # def evaluate_print_func(self, node):
    #     list = node.listOfLists[0]
    #     printLine = ""
    #     for expr in list:
    #         printLine += str(expr.accept(self))
    #         printLine += "|"
    #     printLine = printLine[:-1]
    #     print(printLine)
    #     return printLine

    def evaluate_function_decl(self, node):
        self.funcBinding.push()
        self.funcBinding.set_variable(node.name, [node.paramList, node.CodeBlock])
        print("function bindings: ", self.funcBinding.bindings)

    def evaluate_function_call(self, node):
        function = self.funcBinding.get_variable_value(node.name)
        parameters = function[0]
        code = function[1]
        tempBinding = self.varBinding.bindings.copy()
        
        index = 0
        for params in parameters:
            tempBinding[params] = node.args[index].accept(self)
            index += 1
        print(self.varBinding.bindings)
        print(tempBinding)
        return code.accept(self)

    # def evaluate_statement(self, node):
    #     for decl in node.list:
    #         decl.accept(self)

# @dataclass
# class Thunk():
#     formal_params: List[str]
#     body: "Code"
#     defining_binding: Binding

