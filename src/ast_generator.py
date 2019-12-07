# This file is the parser

from arpeggio import PTNodeVisitor
from objects import *


def binop_list(children):
  child = children[0]

  length = len(children)
  offset = 1
  while offset < length:
    op = children[offset]
    right = children[offset + 1]
    child = BinOpNode(child, op, right)
    offset += 2
  return child


class VisitorClass(PTNodeVisitor):

  def visit_code(self, node, children):
    return Code(children)

  def visit_arithmetic_expr(self, node, children):
    return binop_list(children)

  def visit_variable_value(self, node, children):
    return VariableNode(children[0])

  def visit_mult_term(self, node, children):
    return binop_list(children)

  def visit_integer(self, node, children):
    if children[0] == '-':
      return IntegerNode(-int(children[1]))
    else:
      return IntegerNode(int(children[0]))

  def visit_assignment(self, node, children):
    if self.debug:
      print("assign: {}".format(children))
    return AssignmentNode(children[0], children[1])

  def visit_variable_decl(self, node, children):
    return VariableDeclNode(children)

  def visit_decl(self, node, children):
    if self.debug:
      print("decl: {}".format([children,node.value]))
    if len(children) == 1:
      return DeclNode(children[0])
    else:
      return DeclNode(children[0], children[1])

  def visit_variable_reference(self, node, children):
    if self.debug:
      print("var ref: {}".format(node.value))
    return VariableNode(node.value)

  def visit_function_call(self, node, children):
    if self.debug:
      print("Func call: {}".format(children[0].name))
    if len(children) == 1:
      return FunctionCallNode(children[0].name)
    else:
      return FunctionCallNode(children[0].name, children[1])

  def visit_function_def(self, node, children):
    return FunctionDefNode(children[0], children[1])

  def visit_if_expr(self, node, children):
    if len(children) == 2:
      return IfExprNode(children[0], children[1])
    else:
      return IfExprNode(children[0], children[1], children[2])

  def visit_param_list(self, node, children):
    params = [VariableNode(child) for child in children]
    return params

  def visit_call_arguments(self, node, children):
    if self.debug:
      print(f"visit call: {children}")
    args = [child for child in children]
    return args

  def visit_boolean_expr(self, node, children):
    if self.debug:
      print(f"visit bool expr: {children}")
    return RelOpNode(children[0], children[1], children[2])