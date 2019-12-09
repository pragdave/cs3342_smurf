from math import trunc
from dataclasses import dataclass

bin_ops = {
      "+": lambda l, r: l + r,
      "-": lambda l, r: l - r,
      "*": lambda l, r: l * r,
      "/": lambda l, r: trunc(l/r),
}

rel_ops = {
      "==": lambda l, r: l == r,
      "!=": lambda l, r: l != r,
      ">=": lambda l, r: l >= r,
      "<=": lambda l, r: l <= r,
      ">": lambda l, r: l > r,
      "<": lambda l, r: l < r,
}

#define node types

class Expr():
      def __init__(self,expr_value):
            self.expr_value = expr_value

class Code:
      def __init__(self,statements):
            self.statements = statements
      
      def accept(self, visitor):
            return visitor.evaluate_code(self)


@dataclass
class Integer():
      value: int

      def accept(self, visitor):
            return visitor.evaluate_integer(self)

@dataclass
class BinOp():
      left:       'Expr'
      op:         str
      right:      'Expr'

      def accept(self, visitor):
            return visitor.evaluate_bin_op(self)

@dataclass
class RelOp():
      left:       'Expr'
      op:         str
      right:      'Expr'

      def accept(self, visitor):
            return visitor.evaluate_rel_op(self)

@dataclass
class Assignment():
      varname:   str
      varexp:    'Expr'

      def accept(self, visitor):
            return visitor.evaluate_assignment(self)


@dataclass
class IfNode():
      condSt:    'Expr'
      thenSt:    'Expr'

      def accept(self, visitor):
            return visitor.evaluate_if_expression(self)

@dataclass
class IfElseNode():
      condSt:     'Expr'
      thenSt:     'Expr'
      elseSt:     'Expr'

      def accept(self, visitor):
            return visitor.evaluate_if_else_expression(self)

@dataclass
class DeclNode():
      name:       'Expr'
      value:       'Expr'

      def accept(self, visitor):
            return visitor.evaluate_decl(self)

class VariableDeclNode:
      def __init__(self, decls):
            self.decls = decls
      
      def accept(self, visitor):
            #list of declarations- loop through them
            #need to return the last value
            finalValue = None
            for declaration in self.decls:
                  finalValue = declaration.accept(visitor)
            return finalValue

@dataclass
class VarNode():
      name: str

      def accept(self, visitor):
            return visitor.evaluate_variable(self)

class FunctionDefNode:
      def __init__(self, params, body):
            self.params = params
            self.body = body

      def accept(self, visitor):
            return visitor.evaluate_function_definition(self)

class Thunk:
      def __init__(self, params, body, binding):
            self.params = params
            self.body = body
            self.defining_binding = binding
      
      def accept(self, visitor, args):
            return visitor.evaluate_thunk(self, args)

class FunctionCallNode:
      def __init__(self, name, args = []):
            self.name = name
            #if it's not a list, we make it a list so that we can loop through it even if there's only 1 argument
            if type(args) != list:
                  self.args = [args]
            else:
                  self.args = args
            
      def accept(self, visitor):
            return visitor.evaluate_function_call(self)

            