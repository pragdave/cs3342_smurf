
from Objects import Thunk
class Binding:
    def __init__(self, outer = None):
        self.bindings = {}
        self.outer = outer

    def push(self):
        return Binding(self)

    def pop(self):
        return self.outer

    def set_variable(self, name, value):
        self.bindings[name] = value
        return value

    def get_value(self, name):
        if name in self.bindings:
            return self.bindings[name]
        elif self.outer:
            return self.outer.get_value(name)
        else:
            raise Exception("Variable {0} is not defined".format(str(name)))


class Interpreter:
    def __init__(self):
        self.binding = Binding({})

    def interpret_code(self, node):
        for stmnt in node.statements:
            value = stmnt.eval(self)
        return value

    def interpret_variable(self, node):
        return self.binding.get_value(node.name)

    def interpret_integer(self, node):
        return node.value
    
    def interpret_binop(self, node):
        if node.left is None or node.right is None:
            raise Exception("left or right binary operation is invalid")
        return node.binary_operators[node.op](node.left.eval(self), node.right.eval(self))

    def interpret_relop(self, node):
        if node.left is None or node.right is None:
            raise Exception("left or right comparison operation is invalid")
        return node.comparison_operators[node.op](node.left.eval(self), node.right.eval(self))

    def interpret_assignment(self, node):
        return self.binding.set_variable(node.name, node.expr.eval(self))

    def interpret_decl(self, node):
        set_result = node.expr
        if set_result:
            set_result = node.expr.eval(self)
        return self.binding.set_variable(node.name, set_result)

    def interpret_function_call(self, node):
        arg_values = [arg.eval(self) for arg in node.args]
        thunk = self.binding.get_value(node.name)
        return thunk.eval(self, arg_values)

    def interpret_function_def(self, node):
        return Thunk(node.params, node.body, self.binding)
    
    def interpret_print_call(self, node):
        arg_values = [arg.eval(self) for arg in node.args]
        result = "Print: "
        for i in range(len(arg_values) - 1):
            result += str(arg_values[i]) + "|"
        if len(arg_values) > 0:
            result += str(arg_values[-1])
            print(result)
            return arg_values[-1]
        else:
            print(result)
            return None

    def interpret_if_expr(self, node):
        if node.expr.eval(self):
            return node.then_block.eval(self)
        return None if node.else_block is None else node.else_block.eval(self)

    def interpret_thunk(self, node, args):
        new_binding = self.binding
        self.binding = node.binding.push()
        for i in range(len(args)):
            self.binding.set_variable(node.params[i].name, args[i])
        result = node.body.eval(self)
        self.binding = new_binding
        return result
