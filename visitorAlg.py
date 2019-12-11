from arpeggio import *
from visitorNodes import *
class SmurfVisitor(PTNodeVisitor):
    #result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))
    def visit_program(self, node, children):
        return Program(children[0])

    def visit_code(self, node, children):
        return Code(children)

    def visit_expr(self, node, children):
        if(len(children) == 1): #tells if its a fn or if compared to a arith_expr
            return Expr(children[0])
        else:
            return Expr(children[1])
    
    def visit_arithmetic_expression(self,node,children):
        return Arithmetic_Expressions(children)
    
    def visit_mult_term(self,node,children):
        return Mult_Term(children)
    
    def visit_primary(self,node,children):
        return Primary(children)

    def visit_integer(self,node,children):
        print(f"Visit Integer: {int(node.value)}")
        return Integer(int(node.value))
    
