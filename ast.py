from arpeggio import PTNodeVisitor
from interpreter import *

class Visitor(PTNodeVisitor):
  def visit_code(self, node, children):
    return Code(children)

  def visit_integer(self, node, children):
    if children[0] == '-':
      return Integer(-int(children[1]))
    else:
      return Integer(int(children[0]))
  def visit_assignment(self, node, children):
    return Assignment(children[0], children[1])

  def visit_variable_decl(self, node, children):
    return VariableDecl(children)

  def visit_decl(self, node, children):
    if len(children) == 1:
      return Decl(children[0])
    else:
      return Decl(children[0], children[1])

  def visit_variable_reference(self, node, children):
    return Variable(node.value)

  def visit_arithmetic_expression(self, node, children):
    if (len(children) == 1):
      return children[0]
    else:
      if children[1] == "+":
        return (Plus(children[0], children[2]))
      elif children[1] == "-":
        return (Minus(children[0], children[2]))

  def visit_mult_term(self, node, children):
    if (len(children) == 1):
      return children[0]
    else:
      if children[1] == "*":
        return (Multiply(children[0], children[2]))
      elif children[1] == "/":
        return (Divide(children[0], children[2]))

  def visit_function_call(self, node, children):
    if len(children) == 1:
      return FunctionCall(children[0].name)
    else:
      return FunctionCall(children[0].name, children[1])

  def visit_function_def(self, node, children):
    return FunctionDef(children[0], children[1])

  def visit_if_expr(self, node, children):
    if len(children) == 2:
      return IfExpr(children[0], children[1])
    else:
      return IfExpr(children[0], children[1], children[2])

  def visit_boolean_expression(self, node, children):
    return RelOp(children[0], children[1], children[2])

  def visit_param_list(self, node, children):
    params = [Variable(child) for child in children]
    return params

  def visit_call_arguments(self, node, children):
    args = [child for child in children]
    return args
