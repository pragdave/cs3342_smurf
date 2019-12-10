from arpeggio import PTNodeVisitor
from src.CodeEvaluator import *
from src.ExpressionEvaluator import *
from src.LangEvaluator import *
from src.VariableEvaluator import *


class LangVisitor(PTNodeVisitor):
    def visit_program(self, node, children):
        return (Program(children[0]))

    def visit_code(self, node, children):
        return (Code(children))

    # def visit_variable_declaration(self, node, children):
    #     return (Declaration(children))

    def visit_decl(self, node, children):
        # if len(children) == 1:
        #     return (Decl(children[0], 0))
        # else:
        return (Declaration(children[0], children[1]))

    def visit_identifier(self, node, children):
        return (Terminal(str(node.value)))

    def visit_variable_reference(self, node, children):
        return (VarReference(node.value))

    def visit_if_expression(self, node, children):
        if len(children) == 2:
            return (If_Expression(children[0], children[1]))
        else:
            return (If_Expression(children[0], children[1], children[2]))

    def visit_assignment(self, node, children):
        return (Assignment(children[0], children[1]))

    def visit_boolean_expression(self, node, children):
        left = children[0]
        right = children[2]
        symbol = children[1]
        return BooleanEvaluator(left, right, symbol)

    def visit_arithmetic_expression(self, node, children):
        if len(children) == 1:
            return children[0]
        left = children[0]
        right = children[2]
        symbol = children[1]
        return AddOpEvaluator(left, right, symbol)

    def visit_mult_term(self, node, children):
        if len(children) == 1:
            return children[0]
        left = children[0]
        right = children[2]
        symbol = children[1]
        return MulOpEvaluator(left, right, symbol)

    def visit_integer(self, node, children):
        return Terminal(int(node.value))

    # def visit_function_call(self, node, children):
    #     if len(children) == 1:
    #         return (Function_Call(Call_Arguments([]), children[0]))
    #     else:
    #         return (Function_Call(children[1], children[0]))

    def visit_print_call(self, node, children):
        # if len(children) == 0:
        #     return (Function(Call_Arguments([])))
        # else:
        return (PrintFunction(children[0]))

    # def visit_call_arguments(self, node, children):
    #     return (Call_Arguments(children))

    # def visit_function_definition(self, node, children):
    #     return (Function_Definition(children[0], children[1]))

    # def visit_param_list(self, node, children):
    #     return (Param_List(children))
