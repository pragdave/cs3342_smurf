from Interpreter import *
from Grammar import *
from arpeggio import *

def binop_list(children):
    child = children[0]
    length = len(children)
    for offset in range(1, length, 2):
        op = children[offset]
        right = children[offset+1]
        child = BinopNode(child, op, right)
    return child

class AstVistor(PTNodeVisitor):
    def visit_arithmetic_expression(self, node, children):
        return binop_list(children)

    def visit_multerm(self, node, children):
        return binop_list(children)
    
    def visit_primary(self ,node, children):
        return children[0]

    def visit_integer(self, node, children):
        return IntegerNode(node.value)

   