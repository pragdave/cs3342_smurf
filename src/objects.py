
class Code:
  def __init__(self, statements):
    self.statements = statements

  def accept(self, visitor):
    return visitor.evaluate_code(self)


class StatementNode:
  def __init__(self, statement):
    self.statement = statement

  def accept(self, visitor):
    return visitor.evaluate_statement(self)


class VariableNode:
  def __init__(self, name):
    self.name = name

  def accept(self, visitor):
    return visitor.evaluate_variable(self)


class IntegerNode:
  def __init__(self, value):
    self.value = value

  def accept(self, visitor):
    return visitor.evaluate_integer(self)


class AssignmentNode:
  def __init__(self, name, expr):
    self.name = name
    self.expr = expr

  def accept(self, visitor):
    return visitor.evaluate_assignment(self)


class DeclNode:
  def __init__(self, name, expr = None):
    self.name = name
    self.expr = expr

  def accept(self, visitor):
    return visitor.evaluate_decl(self)


class VariableDeclNode:
  def __init__(self, decls):
    self.decls = decls

  def accept(self, visitor):
    value = None
    for decl in self.decls:
      value = decl.accept(visitor)
    return value


class FunctionCallNode:
  def __init__(self, name, args = []):
    self.name = name
    if type(args) != list:
      self.args = [args]
    else:
      self.args = args

  def accept(self, visitor):
    return visitor.evaluate_function_call(self)


class FunctionDefNode:
  def __init__(self, params, body):
    self.params = params
    self.body = body

  def accept(self, visitor):
    return visitor.evaluate_function_def(self)


class IfExprNode:
  def __init__(self, expr, then_block, else_block = None):
    self.expr = expr
    self.then_block = then_block
    self.else_block = else_block

  def accept(self, visitor):
    return visitor.evaluate_if_expr(self)


class Thunk:
  def __init__(self, params, body, binding):
    self.params = params
    self.body = body
    self.binding_at_def = binding

  def accept(self, visitor, args):
    return visitor.evaluate_thunk(self, args)
    

class BinOpNode:
  ops = {
    "+": lambda l, r: l + r,
    "-": lambda l, r: l - r,
    "*": lambda l, r: l * r,
    "/": lambda l, r: int(l / r)
  }

  def __init__(self, left, op, right):
    self.left = left
    self.op = op
    self.right = right

  def accept(self, visitor):
    return visitor.evaluate_binop(self)

class RelOpNode:
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
