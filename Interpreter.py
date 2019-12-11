# Binding
class Binding:
    def __init__(self, outer=None):
        self.bindings = {}
        self.outer = outer

    def push(self):
        return Binding(self)
    
    def pop(self):
        return self.outer
    
    def set_variable(self, name, value):
        print(f"{name} <- {value}")
        self.bindings[name] = value
        return value
    
    def get_variable(self, name):
        if name in self.bindings:
            return self.bindings[name]
        
        if self.outer:
            return self.outer.get_variable(name)

        raise Exception(f"Variable '{name} is not defined")

class Thunk:
    def __init__(self, params, body, binding):
        self.params = params
        self.body = body
        self.df_binding = binding

    def evaluate(self, args):
        binding = self.df_binding
        binding = binding.push()

        for param, arg in zip(self.params, args):
            binding.set_variable(param, arg)
        
        result = self.body.evaluate(binding)

        binding = binding.pop()
        return result
        
# Node Interpreter
class CodeBlock:
    def __init__(self, expr):
        self.expr = expr
    
    def evaluate(self, binding):
        result = 0
        for e in self.expr:
            result = e.evaluate(binding)
        return result

# ------------------------- function -------------------------
class FunctionDecl:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def evaluate(self,binding):
        return Thunk(self.params, self.body, binding)

class FunctionCall:
    def __init__(self, name, args):
        self.name = name 
        self.args = args

    def evaluate(self, binding):
        pValues = [
            arg.evaluate(binding) for arg in self.args
        ]
        thunk = binding.get_variable(self.name)
        print(thunk)
        return thunk.evaluate(binding, pValues)


# ------------------------- variable -------------------------
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
        return value
        

class VariableReference:
    def __init__(self, name):
        self.name = name
    
    def evaluate(self, binding):
        return binding.get_variable(self.name)

# class VariableNode:
#     def __init__(self, name):
#         self.name = name
    
#     def evaluate(self, binding):
#         return self.value

class IntegerNode:
    def __init__(self, value):
        self.value = value

    def evaluate(self, binding):
        return self.value


# ------------------------- expressions -------------------------
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
    
