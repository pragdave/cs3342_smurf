from arpeggio import *
from interpreter import *


class SmurfVisitor(PTNodeVisitor):
    # result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))
    def visit_program(self, node, children):
        # print(f"visit program children: {children}")
        # print(f"visit program children[0]: {children[0]}")
        if(len(children) > 0):
            return Program(node,children[0])
        else: 
            return

    def visit_code(self, node, children):
        # print(f"visit code children: {children}")
        # print(f"visit code node: {node}")
        return Code(children)

    def visit_statement(self, node, children):
        # print(f"visit statement children: {children}")
        # print(f"visit statement children[0]: {children[0]}")
        # print(f"visit statement node: {node}")
        #if(children([0]) == "let"):
            #return Variable_Declaration(children)
        if(len(children) > 0):
            return Statement(children[0])
        else:
            return
    def visit_expr(self, node, children):
        # print(f"vist expr children : {children}")
        if (len(children) == 1):  # tells if its a fn or if compared to a arith_expr
            # print(f"visit expr children[0]: {children[0]}")
            # print(f"visit expr node: {node}")
            return Expr(children[0])
        elif len(children) > 0:
            # print(f"visit expr children[1]: {children[1]}")
            # print(f"visit expr node: {node}")
            return Expr(children[1])
        return

    def visit_if_expression(self,node, children):
        # print(f"If Expression Node: {node}")
        # print(f"If Expression Children: {children}")
        return If(children)

    def visit_boolean_expression(self,node,children):
        # print(f"visit boolean expression len.children: {len(children)}")
        # print(f"visit boolean expression children: {children}")
        # print(f"vist boolean node: {node}")
        return Boolean(children[0],children[1] ,children[2])

    def visit_arithmetic_expression(self, node, children):
        # print(f"visit arith expression len.children: {len(children)}")
        # print(f"visit arith expression children: {children}")
        # print(f"vist arith node: {node}")
        #return Arithmetic_Expressions(children)
        if(len(children) == 1):
            return children[0]
        else:
            return AddSub(children[0],children[1] ,children[2])

        print(f"SYNTAX ERROR: INCORRECT ARIHMETIC EXPRESSION")
        return

    def visit_mult_term(self, node, children):
        # print(f"Visit Mult Term children: {children}")
        # print(f"Visit Mult Term node: {node}")
        if (len(children) == 1):
            return children[0]
        else:
            return MultDivide(children[0], children[1], children[2])

    # def visit_primary(self, node, children):
    #     print(f"Visit Primary children: {children}")
    #     return Primary(children)

    def visit_integer(self, node, children):
        # print(f"Visit Integer children: {children}")
        # print(f"Visit Integer node.value: {(node.value)}")
        if (children[0] == '-'):
            # print(f"Returning: {int(node.value[4:]) * -1}")
            return Integer  (int(node.value[4:]) * -1)
        # print(f"Visit Integer: {int(node.value)}")
        return Integer(int(node.value))

    def visit_function_call(self, node, children):
        #print(f"visit function call children: {children}")
        #print(f"visit function call node: {node}")
        if len(children) > 0:
            # print(f"Got into Print If")
            # print(f"function node: {node}")
            return FunctionCall(node[0], children[0])
