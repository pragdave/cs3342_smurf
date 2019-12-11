from arpeggio import PTNodeVisitor
import tree_nodes as nodes
from grammar import *

class Generator(PTNodeVisitor):
    
    def visit_code(self, node, children):
        return nodes.Code(children)
    
    def visit_variable(self, node, children):
        return nodes.Variable(node.value)
    
    def visit_brace_block(self, node, children):
        return nodes.Brace_Block(children)
    
    def visit_assignment(self, node, children):
        if(len(children)) > 2:
            return nodes.Assignment(node, children)
        elif(len(children) == 2):
            return nodes.Assignment(node, children)
    
    def visit_variable_declaration(self, node, children):
        return nodes.Let_Decl(children)
    
    def visit_if_expr(self, node, children):
        if(len(children) > 2):
            return nodes.If_Else(children[0], children[1], children[3])
        else:
            return nodes.If_Expression(children[0], children[1])
    
    def visit_decl(self, node, children):
        if(len(children) == 2):
            return (nodes.Assignment(children[0], children[1]))
        else:
            return (nodes.Declaration(children[0]))
    
    def visit_arithmethic_expression(self, node, children):
        return nodes.Arithmetic_Expression(children[0], children[1:])
    
    def visit_boolean_expression(self, node, children):
        return nodes.Boolean_Expression(children[0], children[1], children[2])
    
    def visit_mult_term(self, node, children):
        return nodes.Mult_Term(children[0], children[1:])
    
    def visit_print_smurf(self, node, children):
        return nodes.Print_Smurf(children)
    
    def visit_primary(self, node, children):
        return children[0]
    
    def visit_integer(self, node, children):
        if(len(children) > 1):
            return nodes.integer(children[1], children[0])
        else:
            return nodes.Integer('+', children[0])
    
    def visit_identifier(self, node, children):
        return nodes.Identifier(children[0])