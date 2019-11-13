from grammar import *

class SmurfVisitor(PTNodeVisitor):

    def visit_integer(self,node,children):
        return int(node.value)


    def visit_mult_term(self,node,children):
        if(len(children) == 1):
            return children[0]
        else:
            if children[1] == "*":
                return (children[0] * children[2])
            elif children[1] == "/":
                return (children[0] / children[2])

    def visit_arithmetic_expression(self,node,children):
        if(len(children) == 1):
            return children[0]
        else:
            if children[1] == "+":
                return (children[0] + children[2])
            elif children[1] == "-":
                return (children[0] - children[2])


    def visit_print(self,node,children):
        print(node.value)
        return (node)


        
    