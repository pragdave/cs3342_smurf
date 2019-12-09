
from objects import *

class Binding:
  def __init__(self, outer = None):
    self.bindings = {}
    self.outer = outer

  def push(self):
    return Binding(self)

  def pop(self):
    return self.outer

  def set_variable(self, name, value):
    self.bindings[name] = value
    return value

  def get_value(self, name):
    if name in self.bindings:
      return self.bindings[name]
    
    if self.outer:
      return self.outer.get_value(name)

    raise Exception(f"Variable '{name}' is not defined")


class Interpreter:
  def __init__(self):
    # interpreter-wide binding
    # using this method because I find it easier and clearer than passing the binding
    # into every function that needs it
    self.binding = Binding()

  def evaluate_code(self, node):
    final_value = 0
    for stmnt in node.statements:
      final_value = stmnt.accept(self)
    return final_value

  def evaluate_variable(self, node):
    return self.binding.get_value(node.name)

  def evaluate_integer(self, node):
    return node.value

  def evaluate_assignment(self, node):
    return self.binding.set_variable(node.name, node.expr.accept(self))

  def evaluate_decl(self, node):
    return self.binding.set_variable(node.name, None if node.expr == None else node.expr.accept(self))

  def evaluate_function_call(self, node):
    # evaluates all of the expressions within the call arguments for the function
    arg_values = [
      arg.accept(self) for arg in node.args
    ]
    if node.name == "print":
      result = "Print: "
      for i in range(0, len(arg_values) - 1):
        result += str(arg_values[i]) + "|"
      result += str(arg_values[-1])
      print(result)
      return arg_values[-1]
    else:
      thunk = self.binding.get_value(node.name)
      return thunk.accept(self, arg_values)

  def evaluate_function_def(self, node):
    return Thunk(node.params, node.body, self.binding)

  def evaluate_if_expr(self, node):
    if node.expr.accept(self):
      return node.then_block.accept(self)
    else:
      if node.else_block is None:
        return
      else:
        return node.else_block.accept(self)

  def evaluate_thunk(self, node, args):
    # stores the current binding for replacement later
    temp_binding = self.binding
    # temporarily changes the current binding to the one at definition
    self.binding = node.binding_at_def
    self.binding = self.binding.push()
    # set all passed in arguments for the new binding
    for formal, actual in zip(node.params, args):
      self.binding.set_variable(formal.name, actual)

    result = node.body.accept(self)
    # sets the class's binding to what it was before the thunk was evaluated
    self.binding = temp_binding
    return result

  def evaluate_binop(self, node):
    left = node.left.accept(self)
    right = node.right.accept(self)
    return node.ops[node.op](left, right)

  def evaluate_relop(self, node):
    left = node.left.accept(self)
    right = node.right.accept(self)
    return node.ops[node.op](left, right)
