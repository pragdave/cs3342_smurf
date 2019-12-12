from arpeggio import PTNodeVisitor as visitor
from checking import *
from codeChecker import *

#define visit for each thing thats implemented so that you can actually use
#them when looking through the tree
class smurfVisitor(visitor):
    def visit_program(self, node, children):
        return (program(children[0]))

    def visit_code(self, node, children):
        return (code(children))

    def visit_variable_declaration(self, node, children):
        return (varDec(children))

    def visit_decl(self, node, children):
        if len(children) == 1:
            return (Declaration(children[0], None))
        else:
            return (Declaration(children[0], children[1]))

    def visit_identifier(self, node, children):
        return (terminal(str(node.value)))

    def visit_variable_reference(self, node, children):
        return (Ref(node.value))

    def visit_if_expression(self, node, children):
        if len(children) == 2:
            return (conditional(children[0], children[1]))
        else:
            return (conditional(children[0], children[1], children[2]))

    def visit_assignment(self, node, children):
        return (Assignment(children[0], children[1]))

    def visit_boolean_expression(self, node, children):
        left = children[0]
        right = children[2]
        symbol = children[1]
        return booleval(left, right, symbol)

    def visit_arithmetic_expression(self, node, children):
        if len(children) == 1:
            return children[0]
        left = children[0]
        right = children[2]
        symbol = children[1]
        return arithmetic_expression(left, right, symbol)

    def visit_mult_term(self, node, children):
        if len(children) == 1:
            return children[0]
        left = children[0]
        right = children[2]
        symbol = children[1]
        return arithmetic_expression(left, right, symbol)

    def visit_integer(self, node, children):
        return terminal(int(node.value))

    def visit_function_call(self, node, children):
        if len(children) == 1:
            return (FunctionCall(children[0], CallArguments([])))
        else:
            return (FunctionCall(children[0], children[1]))

    def visit_print_call(self, node, children):
        if len(children) == 0:
            return (Function(CallArguments([])))
        else:
            return (PrintFunction(children[0]))

    def visit_call_arguments(self, node, children):
        return (CallArguments(children))

    def visit_function_definition(self, node, children):
        return (FunctionDefinition(children[0], children[1]))

    def visit_param_list(self, node, children):
        return (ParamList(children))

    def visit_print_function(self, node, children):
        if len(children) == 0:
            return (PrintFunction(Call_Arguments([])))
        else:
            return (PrintFunction(children[0]))