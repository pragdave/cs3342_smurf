from arpeggio import PTNodeVisitor
import tree_nodes as nodes

class Generator:
    
    def visit_code(self, node, children):
        return nodes.Code(children)
    
    def visit_variable(self, node, children):
        return nodes.Variable(node.value)
    
    def visit_arithmethic_expression(self, node, children):
        return nodes.Arithmetic_Expression(children[0], children[1:])
    
    def visit_boolean_expression(self, node, children):
        return nodes.Boolean_Expression(children[0], children[1], children[2])
    
    def visit_mult_term(self, node, children):
        return nodes.Mult_Term(children[0], children[1:])
    
    def visit_print_smurf(self, node, children):
        return nodes.Print_Smurf(children)
    
    def visit_integer(self, node, children):
        if(len(children) > 1):
            return nodes.integer(children[0], children[1])
        else:
            return nodes.integer(children[0], '+')