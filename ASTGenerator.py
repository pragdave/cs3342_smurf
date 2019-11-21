from arpeggio import PTNodeVisitor
import AstNodes as nodes

class ASTGenerator(PTNodeVisitor):
    ##############
    #Math Portion#
    ##############
    def visit_number(self, node, children):
        return nodes.Number(node.value)
    
    def visit_factor(self, node, children):
        if len(children) == 1:
            return nodes.Factor(children[0], "none")
        if children[0] == '-':
            return nodes.Factor(children[1], "-")
        else:
            return nodes.Factor(children[1], "+")
        
    def visit_mult_term(self, node, children):
        return nodes.Mult_Term(children[0], children[1:])
        
    def visit_arithmetic_expression(self, node, children):
        return nodes.Arithmetic_Expression(children[0], children[1:])
    
    ####################
    #Built in Functions#
    ####################

    def visit_var_decl(self, node, children):
        return nodes.Var_Decl(children[0], children[1])
        
    def visit_var_let(self, node, children):
        return nodes.Var_Let(children)
        
    def visit_boolean_expression(self, node, children):
        if len(children) == 1:
            return nodes.Number(children[0])
        return nodes.Boolean_Expression(children[0], children[1], children[2])
    
    def visit_print_func(self, node, children):
        return nodes.Print_Func(children)
        
    def visit_code_block(self, node, children):
        return nodes.Code_Block(children)
        
    def visit_if_statement(self, node, children):
        return nodes.If_Statement(children[0], children[1], children[2])
        
    def visit_fn_decl(self, node, children):
        numChildren = len(children)
        return nodes.Fn_Decl(children[0], children[1:numChildren-1], children[numChildren-1])
        
    def visit_fn_let(self, node, children):
        return nodes.Fn_Let(children)
        
    def visit_fn_call(self, node, children):
        return nodes.Fn_Call(children[0], children[1])
    
    #########################
    #Non-Interpretable types#
    #########################
    
    def visit_valid_line(self, node, children):
        return children[0]
        
    def visit_evaluatable(self, node, children):
        return children[0]
        
    def visit_func_parameters(self, node, children):
        return children
    
    ####################
    #Top Level Function#
    ####################
    
    def visit_code(self, node, children):
        return nodes.Code(children)