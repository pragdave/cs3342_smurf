# This file is the parser

from arpeggio import PTNodeVisitor
from Objects import *

class VisitorClass(PTNodeVisitor):
    @staticmethod
    def get_ops(children):
        child = None if len(children) == 0 else children[0]

        length = len(children)
        offset = 1
        while offset < length:
            child = BinOp(child, children[offset], children[offset + 1])
            offset += 2
        return child

    def visit_code(self, node, children):
        return Code(children)
    
    def visit_integer(self, node, children):
        return Integer(int(children[1])*-1) if children[0] == "-" else Integer(int(children[0]))
    
    def visit_variable_decl(self, node, children):
        return VariableDecl(children)

    def visit_decl(self, node, children):
        return Decl if len(children) == 1 else Decl(children[0], children[1])
    
    def visit_variable_reference(self, node, children):
        return Variable(node.value)
    
    def visit_arithmetic_expr(self, node, children):
        return VisitorClass.get_ops(children)
    
    def visit_boolean_expr(self, node, children):
        return RelOp(children[0], children[1], children[2]) 
    
    def visit_assignment(self, node, children):
        return Assignment(children[0], children[1])

    def visit_mult_term(self, node, children):
        return VisitorClass.get_ops(children)
    
    def visit_param_list(self, node, children):
        return [Variable(child) for child in children]

    def visit_function_call(self, node, children):
        return FunctionCall(children[0].name) if len(children) == 1 else FunctionCall(children[0].name, children[1])
    
    def visit_function_def(self, node, children):
        return FunctionDef(children[0], children[1])
    
    def visit_print_call(self,node,children):
        return Print(children)

    def visit_if_expr(self, node, children):
        return IfExpr(children[0], children[1]) if len(children) == 2 else IfExpr(children[0], children[1], children[2])

    def visit_call_arguments(self, node, children):
        return [child for child in children]

