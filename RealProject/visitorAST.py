from arpeggio import *
from visitorNodes import *


class SmurfVisitor(PTNodeVisitor):
    # result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))
    def visit_program(self, node, children):
        print(f"visit program children: {children}")
        print(f"visit program node: {node}")
        string = "("
        #string += visit_code() + ")"
        #return string
        #return Program(children[0])

    def visit_code(self, node, children):
        #print(f"visit code")
        return Code(children)

    def visit_statement(self, node, children):
        return Statement(children[0])
    def visit_expr(self, node, children):
        #print(f"vist expr")
        if (len(children) == 1):  # tells if its a fn or if compared to a arith_expr
            return Expr(children[0])
        else:
            return Expr(children[1])

    def visit_arithmetic_expression(self, node, children):
        #print(f"visit arith expression")
        return Arithmetic_Expressions(children)

    def visit_mult_term(self, node, children):
        #print(f"Visit Mult Term")
        return Mult_Term(children)

    def visit_primary(self, node, children):
        #print(f"Visit Primary")
        return Primary(children)

    def visit_integer(self, node, children):
        print(f"Visit Integer: {int(node.value)}")
        return Integer(int(node.value))

    def visit_function_call(self, node, children):
        print(f"visit function call")
        if node[0].value == "print" or node[0].value == "(":
            print(f"Got into Print If")
            return ToConsole(node[0], children[0])
