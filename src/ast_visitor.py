import arpeggio
from arpeggio import PTNodeVisitor, visit_parse_tree
from nodes import *

def binoplist(children):
      child = children[0]
      length = len(children)
      offset = 1
      while offset < length:
            op = children[offset]
            right = children[offset+1]
            child = BinOp(child, op, right)
            offset += 2
      return child


class SmurfVisitor(PTNodeVisitor): #ASTBuilder() in slides
      def visit_code(self, node, children):
            return Code(children)
      def visit_integer(self,node,children):
            if children[0] == '-':
                  return Integer(-int(children[1]))
            else:
                  return Integer(int(children[0]))      
      def visit_mult_term(self, node, children):
            return binoplist(children)
      def visit_arithmetic_expression(self, node, children):
            return binoplist(children)
      def visit_boolean_expression(self, node, children):
            return RelOp(children[0], children[1], children[2])
      def visit_variable_declaration(self, node, children):
            return VariableDeclNode(children)
      def visit_decl(self, node, children):
            if len(children) == 2:
                  return DeclNode(children[0], children[1]) 
            else: 
                  return DeclNode(children[0], None)           
      def visit_assignment(self, node, children):
            return Assignment(children[0], children[1])
            
      def visit_if_expression(self, node, children):
            if len(children) == 2:
                  return IfNode(children[0], children[1])
            else:
                  return IfElseNode(children[0], children[1], children[2])

      def visit_param_list(self, node, children):
            params = [VarNode(child) for child in children]
            return params 

      def visit_variable_reference(self, node, children):
            return VarNode(node.value)
                  
      def visit_function_definition(self, node, children):
            return FunctionDefNode(children[0], children[1])

      def visit_call_arguments(self, node, children):
            arguments = [child for child in children]
            return arguments

      def visit_function_call(self, node, children):
            if len(children) == 2:
                  return FunctionCallNode(children[0].name, children[1])
            else:
                  return FunctionCallNode(children[0].name)
            
