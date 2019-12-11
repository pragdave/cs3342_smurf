class IntNumber:
    def __init__(self, number, sign):
        self.number = number
        self.sign = sign


class Program:
    def __init__(self,node, program):
        self.program = program
        self.node = node
        print(f"Making Program Class: {self.node} and {self.program}")

    def eval(self, binding):
        print(f"ULTIMATE EVALUATION: {self.program.eval(binding)}")
        print(f"Program Eval Not working?")
        return self.program.eval(binding)


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

    def eval(self, binding):
        return self.statement.eval(binding)


class Expr:
    def __init__(self, expr):
        self.expr = expr

    def eval(self, binding):
        return self.expr.eval(binding)


class Arithmetic_Expressions:
    def __init__(self, arith):
        self.arith = arith

    def eval(self, binding):
        print(f"Arithmetic Reached term[0]: {self.arith[0]}")
        print(f"Arithmetic Reached term: {self.arith}")
        return self.arith[0].eval(binding)

class AddSub:
    def __init__(self, term1, sign, term3):
        self.term1 = term1
        self.sign = sign
        self.term3 = term3

    def eval(self, binding):
        if(self.sign == '+'):
            return self.term1.eval(binding) + self.term3.eval(binding)
        else:
            return self.term1.eval(binding) - self.term3.eval(binding)

class MultDivide:
    def __init__(self,term1, sign, term3):
        self.term1 = term1
        self.sign = sign
        self.term3 = term3

    def eval(self, binding):
        if (self.sign == '*'):
            return self.term1.eval(binding) * self.term3.eval(binding)
        else:
            return int(self.term1.eval(binding) / self.term3.eval(binding))

class Mult_Term:
    def __init__(self, multTerm):
        self.multTerm = multTerm

    def eval(self, binding):
        print(f"Mult_Term Reached: ")
        print(f"Mult Term node?: {self.binding}")
        return self.multTerm.eval(binding)


# class Primary:
#     def __init__(self, primary):
#         self.primary = primary
#
#     def eval(self, binding):
#         print(f"Primary Reached self.integer:")
#         return self.primary.eval(binding)


class Integer:
    def __init__(self, num):
        self.num = num

    def eval(self, binding):
        print(f"Integer Class Eval: {int(self.num)}")
        return int(self.num)

class Function_Call:
    def __init__(self, function, arguments):
        self.function = function
        self.arguments = arguments

    def eval(self, binding):
        print(f"self.arguments[0].eval(binding)[0]: {self.arguments[0].eval(binding)[0]}")
        parameters = self.arguments[0].eval(binding)[0]
        print(f"self.parameters[1].eval(binding): {self.parameters[1].eval(binding)}")
        args = self.parameters[1].eval(binding)
        for i in range(len(parameters)):
            binding[parameters[i]] = args[i]
        print(f"returning function_call: {binding[self.function.value][1].eval(binding)}")
        return binding[self.function.value][1].eval(binding)


class ToConsole:
    def __init__(self, function, arguments):
        print(f"Into init ToConsole")
        self.function = function
        self.arguments = arguments

    def eval(self, binding):
        print(f"Into ToConsole")
        print(f"ToConsole function: {self.function}")
        print(f"ToConsole arguments: {self.arguments}")
        print(f"ToConsole binding: {binding}")
        num = self.arguments.eval(binding)
        print(f"ToConsole num: {num}")
        if self.function == "print":
            if type(num) == int:
                print(f"WE ACTUALLY MADE IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(num)
class Variable_Declaration:
    def __init__(self, declarations):
        self.declarations = declarations
    def eval(self, binding):
        for newVariables in self.declarations:
            variable = newVariables.evaluate(binding)
        return variable