from arpeggio import PTNodeVisitor
from tree_nodes import *
from grammar import *

class Visitor(PTNodeVisitor):
    
    def visit_integer(self, node, children):
        return node.value

    def visit_arithmetic_expression(self, node, children):
        if(children[1] == '+'):
            return (Plus(children[0], children[2]))
        if(children[1] == '-'):
            return (Minus(children[0], children[2]))

    def visit_mult_term(self, node, children):
        if(len(children) <= 1):
            if(children[1] == '*'):
                return (Times(children[0], children[2]))
            if(children[1] == '/'):
                return (Divide(children[0], children[2]))
        

    def visit_boolean_expression(self, node, children):
        if(children[1] == '=='):
            return (Equals(children[0], children[2]))
        if(children[1] == '!='):
            return (NotEquals(children[0], children[2]))
        if(children[1] == '>='):
            return (GreaterEquals(children[0], children[2]))
        if(children[1] == '>'):
            return (Greater(children[0], children[2]))
        if(children[1] == '<='):
            return (LessEquals(children[0], children[2]))
        if(children[1] == '<'):
            return (Less(children[0], children[2]))

    def visit_identifier(self, node, children):
        return children

    def visit_decl(self, node, children):
        if(len(children) > 1):
            return (Declaration(children[0], children[2]))
        else:
            return (Identifier(children[0]))

    

















