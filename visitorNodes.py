class IntNumber:
    def __init__(self, number, sign):
        self.number = number
        self.sign = sign


class Program:
    def __init__(self,code):
        self.code = code
    
    def eval(self, binding):
        print(f"Can I do this? {self.code.eval(binding)}")
        return self.code.eval(binding)

class Comment:
    def __init__(self, comment):
        self.comment = comment
class Code:
    def __init__(self, list_statements):
        self.list_statements = list_statements

    def eval(self, binding):
        for statement in self.list_statements:
            value = statement.eval(binding)
        return value
class Statement:
    def __init__(self, statement):
        self.statement = statement
    def eval(self,binding):
        return self.statement.eval(binding)

class Expr:
    def __init__(self, expr):
        self.expr = expr
    def eval(self, binding):
        return self.expr.eval(binding)

class Arithmetic_Expressions:
    def __init__(self, term):
        self.term = term
    def eval(self, binding):
        print(f"Arithmetic Reached: {self.term[0]}")
        return self.term[0].eval(binding)
class Mult_Term:
    def __init__(self, primary):
        self.primary = primary
    def eval(self, binding):
        print(f"Mult_Term Reached: {self.primary}")
        return self.primary.eval(binding)

class Primary:
    def __init__(self, integer):
        self.integer = integer

    def eval(self, binding):
        print(f"Primary Reached self.integer: {self.integer}")
        return  self.integer.eval(binding)

class Integer:
    def __init__(self, num):
        self.num = num
    def eval(self, binding):
        print(f"Integer Class Eval: {int(self.num)}")
        return int(self.num)

class ToConsole:
    def __init__(self, function, arguments):
        self.function = function
        self.arguments = arguments

    def eval(self, binding):
        nums = self.arguments.eval(binding)
        if self.function == "print":
            if type(nums) == int:
                print(nums)