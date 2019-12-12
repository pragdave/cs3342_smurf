import math 

#THESE CLASSES ARE ALL ABOUT BEGINING THE BINDING PROCESS THAT IS LATER FINSIHED IN TEH INTERPRETER

class Assignment:
  def __init__(self, name, value):
    self.name = name
    self.value = value

  def accept(self, visitor):
      return visitor.evaluate_assignment(self)


class VariableReference:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
      return visitor.evaluate_variable_reference(self)

#NODE TO SET INTEGER BASED ON VALUE  SENT
class Integer:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_integer(self)

#ALL BINARY OPERATIONS
class BinOp:
    ops = {
        "+": lambda l, r: l + r,
        "-": lambda l, r: l - r,
        "*": lambda l, r: l * r,
        "/": lambda l, r: math.trunc(l/r),
    }
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.evaluate_binop(self)

class CodeBlock:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_code(self)

class Program:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_program(self)


class VariableDeclaration:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_variable_declaration(self)

#THIS NODE TAKES IN A NAME AND ITS VALUES AND THE DECLARES THE IN THE INTERPRETER
#SETS THEM TO SELF. VALUE AND SELF.NAME
class Decl:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_decl(self)

#HAD ALOT OF TROUBLE DECLARING VARIABLES SO HAVE THIS FOR SMALL DECALERS
class LetDecl:
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.evaluate_let_decl(self)

#USES THE FUNCTION DEFINITION LOGIC THAT WE LEARNED IN CLASS
class FunctionDefinition:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def accept(self, visitor):
        return visitor.evaluate_function_definition(self) 

#USES THE FUNCTION CALL LOGIC THAT WE LEARNED IN CLASS
class FunctionCall:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def accept(self, visitor):
        return visitor.evaluate_function_call(self)


#USES THE THUNK LOGIC THAT WE LEARNED IN CLASS
class Thunk:
    def __init__(self, params, body, defining_binding):
        self.params = params
        self.body = body
        self.defining_binding = defining_binding

    def accept(self, visitor, values):
        return visitor.evaluate_thunk(self, values)

class PrintCall:
    def __init__(self, value = []):
        #KEPT ERRORING HERE HAD TO 
        #CHECK IF IT IS A LIST OR NOT
        if type(value) == list:
            self.value = value
        else:
            self.value = [value]


    def accept(self, visitor):
        return visitor.evaluate_print_call(self)


#SAME INTANTIOATION AS BIN OP
class RelOp:
    ops = {
        "==": lambda l, r: l == r,
        "!=": lambda l, r: l != r,
        ">=": lambda l, r: l >= r,
        ">" : lambda l, r: l >  r,
        "<=": lambda l, r: l <= r,
        "<" : lambda l, r: l < r
    }

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.evaluate_relop(self)

