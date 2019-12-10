# Binding
class Binding:
    def __init__(self):
        self.bindings = {}
    
    def set_variable(self, name, value):
        print(f"{name} <- {value}")
        self.bindings[name] = value
    
    def get_variable(self, name):
        value = self.bindings.get(name, 0)
        return value

# Node Interpreter
class CodeBlock:
    def __init__(self, expr):
        self.expr = expr
    
    def evaluate(self, binding):
        result = 0
        for e in self.expr:
            result = e.evaluate(binding)
        return result

class FunctionDecl:
    def __init__(self, params, body):
        self.paramas = params
        self.body = body

    def evaluate(self,binding):
        return self.body

class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def evaluate(self, binding):
        body = binding.get_variable(self.name)
        return body.evaluate(binding, [])

class VariableDecl:
    def __init__(self, decl):
        self.decl = decl
    
    def evaluate(self, binding):
        for d in self.decl:
            result = d.evaluate(binding)
        return result

class Decl:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    
    def evaluate(self, binding):
        # refName = self.name.evaluate(binding)
        value = self.expr.evaluate(binding)
        binding.set_variable(self.name, value)
        return value


class Assignment:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
    
    def evaluate(self, binding):
        # refName = self.name.evaluate(binding)
        value = self.expr.evaluate(binding)
        binding.set_variable(self.name, value)
        # return value
        

class VariableReference:
    def __init__(self, name):
        self.name = name
    
    def evaluate(self, binding):
        return binding.get_variable(self.name)

# class Identifier:
#     def __init__(self, value):
#         self.value = value
    
#     def evaluate(self, binding):
#         return self.value

class IntegerNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self, binding):
        return self.value

# Arithemetic Operation
class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return (self.left.evaluate(binding) + self.right.evaluate(binding))

class Subtract:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return (self.left.evaluate(binding) - self.right.evaluate(binding))

class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, binding):
        return (self.left.evaluate(binding) * self.right.evaluate(binding))

class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, binding):
        return int(self.left.evaluate(binding) / self.right.evaluate(binding))
    
