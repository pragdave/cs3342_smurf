from arpeggio import PTNodeVisitor
from tree_nodes import *
from grammar import *

class Visitor(PTNodeVisitor):
    def visit_code(self, node, children):
        return Code(self)

    def visit_assignment(self, node, children):
        if(len(children)) > 2:
            return 
        elif(len(children) == 2):
            return Assignment(node, children)
    
    def visit_print_smurf(self, node, children):
        print(children[0].value)
    
    def visit_variable_value(self, node, children):
        return Variable(node.value)
    
    def visit_integer(self, node, children):
        return Integer(int(node.value))

    def visit_arithmetic_expression(self, node, children):
        if(len(children) > 1):
            if(children[1] == '+'):
                return (Plus(children[0], children[2]))
            if(children[1] == '-'):
                return (Minus(children[0], children[2]))
        else:
            return Integer(node.value)

    def visit_mult_term(self, node, children):
        if(len(children) > 1):
            if(children[1] == '*'):
                return (Times(children[0], children[2]))
            if(children[1] == '/'):
                return (Divide(children[0], children[2]))
        else:
            return Integer(int(node.value))
        
    def visit_primary(self, node, children):
        return children[0]

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
        if(len(children) > 2):
            return (Assignment(children[0], children[2]))
        else:
            return (Assignment(children[0], 0))

    

















