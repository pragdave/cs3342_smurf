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
        return value

    def get(self, name):
        if name in self.bindings:
            return self.bindings[name]

        if self.outer:
            return self.outer.get(name)


# Acts as the high level interpreter to hold current binding state throughout execution.
class Interpreter:
    def __init__(self):
        self.binding = Binding()

    def evaluate_code(self, node):
        final_value = 0
        for stmnt in node.statements:
            final_value = stmnt.evaluate(self)
        return final_value

    def evaluate_variable(self, node):
        return self.binding.get(node.name)

    def evaluate_integer(self, node):
        return node.value

    def evaluate_assignment(self, node):
        return self.binding.set_variable(node.name, node.expr.evaluate(self))

    def evaluate_decl(self, node):
        return self.binding.set_variable(node.name, None if node.expr == None else node.expr.evaluate(self))

    def evaluate_function_call(self, node):
        arg_values = [arg.evaluate(self) for arg in node.args]
        if node.name == "print":
            result = "Print: "
            for i in arg_values:
                result += str(i) + "|"
            result += str(arg_values[-1])
            print(result)
            return arg_values[-1]
        else:
            pb = self.binding.get(node.name)
            return pb.evaluate(self, arg_values)

    def evaluate_function_def(self, node):
        return PBinding(node.params, node.body, self.binding)

    def evaluate_if_expr(self, node):
        if node.expr.evaluate(self):
            return node.then_block.evaluate(self)
        else:
            if node.else_block is None:
                return
            else:
                return node.else_block.evaluate(self)

    def evaluate_PBinding(self, node, args):
        temp_binding = self.binding #save binding
        self.binding = node.binding_at_def
        self.binding = self.binding.push()
        for formal, actual in zip(node.params, args):
            self.binding.set_variable(formal.name, actual)
        result = node.body.evaluate(self)
        self.binding = temp_binding
        return result

    def evaluate_relop(self, node):
        left = node.left.evaluate(self)
        right = node.right.evaluate(self)
        return node.ops[node.op](left, right)


class Code:
    def __init__(self, statements):
        self.statements = statements

    def evaluate(self, visitor):
        return visitor.evaluate_code(self)


class Variable:
    def __init__(self, name):
        self.name = name

    def evaluate(self, visitor):
        return visitor.evaluate_variable(self)


class Integer:
    def __init__(self, value):
        self.value = value

    def evaluate(self, visitor):
        return visitor.evaluate_integer(self)


class Assignment:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def evaluate(self, visitor):
        return visitor.evaluate_assignment(self)


class Decl:
    def __init__(self, name, expr=None):
        self.name = name
        self.expr = expr

    def evaluate(self, visitor):
        return visitor.evaluate_decl(self)


class VariableDecl:
    def __init__(self, decls):
        self.decls = decls

    def evaluate(self, visitor):
        value = None
        for decl in self.decls:
            print(f"vnode decl: {decl}")
            value = decl.evaluate(visitor)
        return value


class FunctionCall:
    def __init__(self, name, args=[]):
        self.name = name
        if type(args) != list:
            self.args = [args]
        else:
            self.args = args

    def evaluate(self, visitor):
        return visitor.evaluate_function_call(self)



class FunctionDef:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def evaluate(self, visitor):
        return visitor.evaluate_function_def(self)


class IfExpr:
    def __init__(self, expr, then_block, else_block=None):
        self.expr = expr
        self.then_block = then_block
        self.else_block = else_block

    def evaluate(self, visitor):
        return visitor.evaluate_if_expr(self)

class PBinding:
    def __init__(self, params, body, binding):
        self.params = params
        self.body = body
        self.binding_at_def = binding

    def evaluate(self, visitor, args):
        return visitor.evaluate_PBinding(self,args)

# +/-/*//
##############
class Plus:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return self.leftside.evaluate(binding) + self.rightside.evaluate(binding)

class Minus:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return self.leftside.evaluate(binding) - self.rightside.evaluate(binding)

class Multiply:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return self.leftside.evaluate(binding) * self.rightside.evaluate(binding)

class Divide:
    def __init__(self,leftside,rightside):
        self.leftside = leftside
        self.rightside = rightside

    def evaluate(self, binding):
        return int(self.leftside.evaluate(binding) / self.rightside.evaluate(binding))
###############

# '==' / '!=' / '>=' / '>' / '<=' / '<'
class RelOp:
    ops = {"==": lambda l, r: l == r, "!=": lambda l, r: l != r, ">=": lambda l, r: l >= r, ">": lambda l, r: l > r,
        "<=": lambda l, r: l <= r, "<": lambda l, r: l < r}

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, visitor):
        return visitor.evaluate_relop(self)


