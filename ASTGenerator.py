from arpeggio import PTNodeVisitor
from AstNodes import Number, Factor, Term, Arithmetic_Expression, Print, Code

class ASTGenerator(PTNodeVisitor):
    def visit_number(self, node, children):
        return Number(node.value)
    
    def visit_factor(self, node, children):
        if len(children) == 1:
            return Factor(children[0], "none")
        if children[0] == '-':
            return Factor(children[1], "-")
        else:
            return Factor(children[1], "+")
        
    def visit_term(self, node, children):
        return Term(children[0], children[1:])
        
    def visit_arithmetic_expression(self, node, children):
        return Arithmetic_Expression(children[0], children[1:])
        
    def visit_print_func(self, node, children):
        return Print(children[0])
        
    def visit_code(self, node, children):
        return Code(children)