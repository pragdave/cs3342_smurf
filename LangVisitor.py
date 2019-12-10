from arpeggio import PTNodeVisitor
from LangInterpreter import *


class LangVisitor(PTNodeVisitor):
    userVars = {}

    def visit_program(self, node, children):
        state = "runNow"

    # def visit_comment(self, node, children):
    #
    # def visit_code(self, node, children):
    #
    def visit_statement(self, node, children):
        print("statement")
    #
    # def visit_variable_declaration(self, node, children):
    #

    def visit_decl(self, node, children):
        if len(children) > 1:
            self.userVars[str(children[0])] = children[1]

    # def visit_identifier(self, node, children):
    #
    # def visit_variable_reference(self, node, children):
    #
    # def visit_if_expression(self, node, children):
    #
    # def visit_assignment(self, node, children):
    #
    # def visit_expr(self, node, children):
    #
    # def visit_boolean_expression(self, node, children):
    #
    # def visit_arithmetic_expression(self, node, children):
    #
    # def visit_mult_term(self, node, children):
    #
    # def visit_primary(self, node, children):
    #

    # def visit_integer(self, node, children):
    #
    # def visit_addop(self, node, children):
    #
    # def visit_mulop(self, node, children):
    #

    def visit_boolean_expression(self, node, children):
        ls = children[0]
        print(ls.evaluate())
        rs = children[2]
        symbol = children[1]
        return BooleanEvaluator(ls, rs, symbol)

    def visit_function_call(self, node, children):
        print("Function call")
    # def visit_call_arguments(self, node, children):
    #

    #
    # def visit_param_list(self, node, children):

    def visit_brace_block(self, node, children):
        print("brace block")

    def visit_function_definition(self, node, children):
        print("Function definition: ")
