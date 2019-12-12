from arpeggio     import PTNodeVisitor
from nodes    import *

#BINOP LIST LIKE FROM THE POWERPOINTS
def binop_tree_from_child_list(children):
    child = children[0]
    length = len(children)
    offset = 1
    while offset < length:
        op = children[offset]
        right = children[offset+1]
        child = BinOp(child, op, right)
        offset += 2
    return child
    

#WHERE THE PARSING HAPPENS
class Visitor(PTNodeVisitor):
    
    ##CODE##
    def visit_code(self, node, children):
        returnCode = CodeBlock(children)
        return returnCode

     ##ASSIGNMENT##
    def visit_assignment(self, node, children):
        returnAssignment = Assignment(children[0], children[1]) 
        return returnAssignment

    def visit_boolean_expr(self, node, children):
        #SENDS IN ALL THRE VALUES IN BOOL EXORESSION
        returnBool =RelOp(children[0], children[1], children[2])
        return returnBool


     ##VARIABLE REFERENCE##
    def visit_variable_reference(self, node, children):
        returnVR  =VariableReference(node.value) 
        return returnVR

     ##EXPR##    
    def visit_expr(self, node, children):
        returnExpr= binop_tree_from_child_list(children)
        return returnExpr

    ##MULT##
    def visit_mult_term(self, node, children):
        returnMult =binop_tree_from_child_list(children)
        return returnMult

     ##PRIMARY##
    def visit_primary(self, node, children):
        returnPrimary =children[0]
        return returnPrimary

     ##INT##       
    def visit_integer(self, node, children):
        if children[0] == "-":
            returnInt =Integer(-int(children[1]))
        else:
            returnInt= Integer(int(children[0])) 

        return returnInt


     ##VARIABLE DECLERATION##
    def visit_variable_declaration(self, node, children):
        returnVD =VariableDeclaration(children)
        return returnVD

     ##DECL##
    def visit_decl(self, node, children):
        if len(children) != 1:
            returnDecl =Decl(children[0], children[1])
        else:
            returnDecl =LetDecl(children[0])

        return returnDecl

     ##FUNCTION DEFINITION##
    def visit_function_definition(self, node, children):
        if len(children) > 1:
            returnFD =FunctionDefinition(children[0], children[1])
        else:
            returnFD =FunctionDefinition(None, children[0])

        return returnFD

 ##FUNCTION CALL##
    def visit_function_call(self, node, children):
        if children[0].name == 'print':
            #SENDING SECOND CHILD IS THE VALUE
            return PrintCall(children[1])
        if len(children) > 1:
            #HAVE TO SEND NAME BECAUSE THE CHILD IS THE OVERALL VALUE
            #WHICH DOSENT HALP IN THIS FUNCTION
            return FunctionCall(children[0].name, children[1])
        else:
            return FunctionCall(children[0].name)

 ##ARITHMETIC EXPRESSION##
    def visit_arithmetic_expression(self, node, children):
        returnAE =binop_tree_from_child_list(children)
        return returnAE
        
