from Interpreter import *
from Grammar import *

# def binop_list(children):
#     child = children[0]
#     length = len(children)
#     for offset in range(1, length, 2):
#         op = children[offset]
#         right = children[offset+1]
#         child = BinopNode(child, op, right)
#     return child

class AstVistor(PTNodeVisitor):
    def visit_arithmetic_expression(self, node, children):
        print('addop')
        if len(children) > 1:
            if children[1] == '+':
                return (Add(children[0],children[2]))
            else:
                return (Subtract(children[0],children[2]))
        else:
            return children[0]

    def visit_multerm(self, node, children):
        print('mulop')
        if len(children) > 1:
            if children[1] == '*':
                return (Multiply(children[0],children[2]))
            else:
                return (Divide(children[0],children[2]))
        else:
            return children[0]
    
    def visit_primary(self ,node, children):
        print('primary')
        return children[0]

    def visit_integer(self, node, children):
        print('int')
        return IntegerNode(int(node.value))

   