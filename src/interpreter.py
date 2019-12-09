from nodes import *
import math

class Binding:
      def __init__(self, outer=None):
            self.bindings = {} #create initial binding
            self.outer = outer #doesn't have to have an outer binding

      def push(self):
            return Binding(self)
      
      def pop(self):
            return self.outer

      def set_variable(self, name, value):
            self.bindings[name] = value
            return value
      
      def get_variable_value(self, name):
            if name in self.bindings:
                  return self.bindings[name] #continue to check recursively bindings outside ours
            if self.outer:
                  return self.outer.get_variable_value(name)
            raise Exception(f"Variable '{name}' is not defined")

class Interpreter:
      def __init__(self):
            self.binding = Binding()

      def evaluate_integer(self,node):
            return node.value
      def evaluate_bin_op(self,node):
            left = node.left.accept(self)
            right = node.right.accept(self)
            return bin_ops[node.op](left,right)
      def evaluate_code(self, node):
            statementval = 0
            for ministatement in node.statements:
                  statementval = ministatement.accept(self)
            return statementval
      def evaluate_rel_op(self, node):
            left = node.left.accept(self)
            right = node.right.accept(self)
            return rel_ops[node.op](left,right)
      def evaluate_assignment(self, node):
            return self.binding.set_variable(node.varname, node.varexp.accept(self))
      def evaluate_if_expression(self, node):
            if node.condSt.accept(self):
                  return node.thenSt.accept(self)
      def evaluate_if_else_expression(self, node): 
            if node.condSt.accept(self):
                  return node.thenSt.accept(self)
            else:
                  return node.elseSt.accept(self)
      
      def evaluate_decl(self, node):
            return self.binding.set_variable(node.name, None if node.value == None else node.value.accept(self))

      def evaluate_variable(self, node):
            return self.binding.get_variable_value(node.name)

      def evaluate_function_definition(self, node):
            return Thunk(node.params, node.body, self.binding)


      def evaluate_thunk(self, node, args):
            temporary = self.binding
            self.binding = node.defining_binding
            #add new layer of bindings
            self.binding = self.binding.push()

            for formal, actual in zip(node.params, args):
                  self.binding.set_variable(formal.name, actual)
            #get result based on new binding
            result = node.body.accept(self)
            self.binding = temporary
            return result

      def evaluate_function_call(self, node):
            argList = [arg.accept(self) for arg in node.args]
            #if it is print function, we need to print stuff
            if node.name == "print":
                  result = "Print: "
                  for i in range(0, len(argList) - 1):
                        result += str(argList[i]) + "|"
                  #we miss the last one so we don't have an extra bar
                  result += str(argList[-1])
                  print(result)
                  return argList[-1]
            else:
                  new_thunk = self.binding.get_variable_value(node.name)
                  return new_thunk.accept(self, argList)



            
