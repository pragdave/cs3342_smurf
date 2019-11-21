from arpeggio import ParserPython, PTNodeVisitor, visit_parse_tree
from AstNodes import *

class NodeVisitor(PTNodeVisitor):
    def visit_start(self, node, children):
        return children[0]

    def visit_assignment(self, node, children):
        return Assignment(children[0], children[1])

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

    # #multuple let
    def visit_variable_declaration(self, node, children):
        return VariableDeclaration(children)

    def visit_code(self, node, children):
        return Code(children)

    def visit_function_definition(self, node, children):
        if len(children) > 1:
            return FunctionDecl(children[0], children[1])
        else:
            return FunctionDecl(None, children[0])

    def visit_function_call(self, node, children):
        if len(children) > 1:
            return FunctionCall(children[0].name, children[1])
        else:
            return FunctionCall(children[0].name)

    def visit_print_function(self, node, children):
        return PrintFunc(children)

    def visit_param_list(self, node, children):
        params = []
        for child in children:
            params.append(VariableReference(child))
        return params

    def visit_decl(self, node, children):
        if len(children) > 1:
            return Declaration(children[0], children[1])
        else:
            return SimpleDeclaration(children[0])

    def visit_call_arguments(self, node, children):
        args = []
        for child in children:
            args.append(child)
        return args