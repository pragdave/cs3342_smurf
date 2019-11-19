from arpeggio import ParserPython, PTNodeVisitor, visit_parse_tree
from AstNodes import *

class NodeVisitor(PTNodeVisitor):
    def visit_start(self, node, children):
        return children[0]

    # def visit_assignment(self, node, children):
    #     return Assignment(children[0], children[1])

    def visit_integer(self, node, children):
        if children[0] == '-':
            return Integer(-int(children[1]))
        else:
            return Integer(int(children[0]))

    def visit_if_expression(self, node, children):
        if len(children) < 3:
            return If(children[0], children[1])
        else:
            return IfElse(*children)

    # def visit_expr(self, node, children):
    #     return binop_list(children)

    def visit_mult_term(self, node, children):
        return binop_list(children)

    def visit_arithmetic_expression(self, node, children):
        return binop_list(children)

    def visit_primary(self, node, children):
        return children[0]

    def visit_boolean_expression(self, node, children):
        return relop_list(children)

    def visit_variable_reference(self, node, children):
        return VariableReference(node.value)

    def visit_code(self, node, children):
        return Code(children)

    def visit_function_call(self, node, children):
        return FunctionCall(children[0], children[1])

    # def visit_statement(self, node, children):
    #     if children[0] == "let":
    #         return Statement(children)
    #     elif children[1] == "=":
    #         return Assignment(children[0], children[1])
    #     else:
    #         binop_list(children)

    def visit_decl(self, node, children):
        if len(children) > 1:
            return Declaration(children[0], children[1])
        else:
            return SimpleDeclaration(children[0])