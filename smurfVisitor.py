from smurf import *
from smurfInterpreter import *

class SmurfVisitor(PTNodeVisitor):
    # def visit_xxx(self,node,children):
    #     return node

    def visit_integer(self,node,children):
        return Integer(int(node.value))

    def visit_primary(self,node,children):
        if len(children) == 1:
            return children[0]
        else:
            return children[1]

    def visit_mult_term(self,node,children):
        if len(children) == 1:
            return children[0]
        else:
            if children[1] == "*":
                return (Times(children[0],children[2]))
            elif children[1] == "/":
                return (Divide(children[0],children[2]))
                
    def visit_arithmetic_expression(self,node,children):
        if len(children) == 1:
            return children[0]
        else:
            if children[1] == "+":
                return (Plus(children[0],children[2]))
            elif children[1] == "-":
                return (Minus(children[0],children[2]))

    def visit_boolean_expression(self,node,children):
        if children[1] == "==":
            return (Equal(children[0],children[2]))
        elif children[1] == "!=":
            return (NotEqual(children[0],children[2]))
        elif children[1] == ">=":
            return (GreaterEqual(children[0],children[2]))
        elif children[1] == ">":
            return (Greater(children[0],children[2]))
        elif children[1] == "<=":
            return (LessEqual(children[0],children[2]))
        elif children[1] == "<":
            return (Less(children[0],children[2]))