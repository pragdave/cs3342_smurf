from Interpreter import *
from arpeggio import PTNodeVisitor
# from Grammar import *

class AstVisitor(PTNodeVisitor):
    def visit_code(self, node, children):
        return CodeBlock(children)

    # ------------------------- function -------------------------
    def visit_function_definition(self, node, children):
        return FunctionDef(children[0], children[1])

    def visit_function_call(self, node, children):
        if len(children) == 1:
            return FunctionCall(children[0].name, [])
        else:
            return FunctionCall(children[0].name, children[1])

    def visit_param_list(self, node, children):
        return children

    def visit_call_arguments(self, node, children):
        return children

    # ------------------------- variable -------------------------
    def visit_variable_declaration(self,node,children):
        return VariableDecl(children)

    # ! optional expr
    def visit_decl(self,node,children):
        return Decl(children[0], children[1])

    def visit_assignment(self, node, children):
        return Assignment(children[0], children[1])

    # def visit_identifier(self,node,children):
    #     return VariableNode(str(node.value))

    def visit_variable_reference(self, node, children):
        return VariableReference(node.value)

    def visit_arithmetic_expression(self, node, children):
        if len(children) > 1:
            if children[1] == '+':
                return (Add(children[0],children[2]))
            else:
                return (Subtract(children[0],children[2]))
        else:
            return children[0]

    def visit_multerm(self, node, children):
        if len(children) > 1:
            if children[1] == '*':
                return (Multiply(children[0],children[2]))
            else:
                return (Divide(children[0],children[2]))
        else:
            return children[0]
    
    def visit_primary(self ,node, children):
        return children[0]

    def visit_integer(self, node, children):
        if children[0] == '-':
            return IntegerNode(-int(children[1]))
        else: 
            return IntegerNode(int(children[0]))

   