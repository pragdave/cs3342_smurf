from arpeggio import PTNodeVisitor
from tree_nodes import *
from grammar import *

class Visitor(PTNodeVisitor):
    def visit_code(self, node, children):
        return Code(children)

    def visit_assignment(self, node, children):
        if(len(children)) > 2:
            return Assignment(node, children)
        elif(len(children) == 2):
            return Assignment(node, children)
    """
    def visit_variable_declaration(self, node, children):
        if(len(children) > 2):
            return Declarations(children[0], children[1:])
    """
    def visit_print_smurf(self, node, children):
        return Print_Smurf(children)
    
    def visit_variable_value(self, node, children):
        return Variable(node.value)
    
    def visit_integer(self, node, children):
        if(len(children)) > 1:
            return Integer(children[0], children[1])
        else:
            return Integer('', children[0])

    def visit_arithmetic_expression(self, node, children):
        return Arithmetic_Expression(children[0], children[1:])

    def visit_mult_term(self, node, children):
        return Mult_Term(children[0], children[1:])
        
    def visit_primary(self, node, children):
        return children[0]

    def visit_boolean_expression(self, node, children):
        return Boolean_Expression(children[0], children[1], children[2])

    def visit_identifier(self, node, children):
        return Identifier(children[0])

    def visit_decl(self, node, children):
        if(len(children) == 2):
            return (Assignment(children[0], children[1]))
        else:
            return (Declaration(children[0]))

    

















