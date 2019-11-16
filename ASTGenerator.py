from arpeggio import PTNodeVisitor
import AstNodes as nodes

class ASTGenerator(PTNodeVisitor):
    def visit_number(self, node, children):
        return nodes.Number(node.value)
    
    def visit_factor(self, node, children):
        if len(children) == 1:
            return nodes.Factor(children[0], "none")
        if children[0] == '-':
            return nodes.Factor(children[1], "-")
        else:
            return nodes.Factor(children[1], "+")
        
    def visit_term(self, node, children):
        return nodes.Term(children[0], children[1:])
        
    def visit_arithmetic_expression(self, node, children):
        return nodes.Arithmetic_Expression(children[0], children[1:])
         
    def visit_var_decl(self, node, children):
        return nodes.Var_Decl(children[0], children[1])
        
    def visit_let(self, node, children):
        return nodes.Let(children)
        
    def visit_boolean_expression(self, node, children):
        return nodes.Boolean_Expression(children[0], children[1], children[2])
    
    def visit_print_func(self, node, children):
        return nodes.Print(children[0], children[1:])
        
    def visit_code(self, node, children):
        return nodes.Code(children)