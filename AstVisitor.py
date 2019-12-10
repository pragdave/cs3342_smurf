from Interpreter import *
from arpeggio import PTNodeVisitor
# from Grammar import *

class AstVisitor(PTNodeVisitor):
    def visit_start(self, node, children):
        return children[0]

    def visit_assignment(self, node, children):
        return Assignment(children[0], children[1])

    def visit_variable_reference(self, node, children):
        return VariableReference(node.value)

    def visit_arithmetic_expression(self, node, children):
        if len(children) > 1:
            if children[1] == '+':
                return (Add(children[0],children[2]))
            else:
                return (Subtract(children[0],children[2]))
        else:
            return children[0]

    def visit_multerm(self, node, children):
        if len(children) > 1:
            if children[1] == '*':
                return (Multiply(children[0],children[2]))
            else:
                return (Divide(children[0],children[2]))
        else:
            return children[0]
    
    def visit_primary(self ,node, children):
        return children[0]

    def visit_integer(self, node, children):
        return IntegerNode(int(node.value))

   