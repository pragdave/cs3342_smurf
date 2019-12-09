from arpeggio import ParserPython, PTNodeVisitor, visit_parse_tree
from AstNodes import *

#This is the parser file for Smurf
class NodeVisitor(PTNodeVisitor):

    def visit_code(self, node, children):
        return CodeNode(children)

    def visit_variable_declaration(self, node, children):
        return VariableDeclarationNode(children)

    def visit_decl(self, node, children):
        if len(children) > 1:
            return DeclarationNode(children[0], children[1])
        else:
            return SimpleDeclarationNode(children[0])

    def visit_variable_reference(self, node, children):
        return VariableReferenceNode(node.value)

    def visit_if_expression(self, node, children):
        if len(children) < 3:
            return IfNode(children[0], children[1])
        else:
            return IfElseNode(*children)

    def visit_assignment(self, node, children):
        return AssignmentNode(children[0], children[1])

    def visit_boolean_expression(self, node, children):
        return RelOpNode(children[0], children[1], children[2])

    def visit_arithmetic_expression(self, node, children):
        return binop_list(children)

    def visit_mult_term(self, node, children):
        return binop_list(children)          

    def visit_integer(self, node, children):
        if children[0] == '-':
            return IntegerNode(-int(children[1]))
        else:
            return IntegerNode(int(children[0]))

    def visit_function_call(self, node, children):
        if len(children) > 1:
            return FunctionCallNode(children[0].name, children[1])
        else:
            return FunctionCallNode(children[0].name)

    def visit_print_function(self, node, children):
        return PrintFunctionNode(children)

    def visit_call_arguments(self, node, children):
        args = []
        for child in children:
            args.append(child)
        return args

    def visit_function_definition(self, node, children):
        if len(children) > 1:
            return FunctionDefinitionNode(children[0], children[1])
        else:
            return FunctionDefinitionNode(None, children[0])

    def visit_param_list(self, node, children):
        params = []
        for child in children:
            params.append(VariableReferenceNode(child))
        return params
