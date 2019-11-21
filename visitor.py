from grammar import *
from interpreter import *

class SmurfVisitor(PTNodeVisitor):

    def visit_program(self,node,children):
        return Program(children[0])


    def visit_code(self,node,children):
        return Code(children)


    def visit_statement(self,node,children):
        return Statement(children[0])


    def visit_variable_declaration(self,node,children):
            return VariableDeclaration(children)

    
    def visit_decl(self,node,children):
        if len(children) == 1:
            return Decl(children[0],0)
        else:
            return Decl(children[0],children[1])


    def visit_identifier(self,node,children):
        return Identifier(node.value)


    def visit_variable_reference(self,node,children):
        return VariableReference(node.value)


    def visit_if_expression(self,node,children):
        return IfExpression(children)


    def visit_assignment(self,node,children):
        return Assignment(children[0],children[1])


    def visit_expr(self,node,children):
        if len(children) == 1:
            return Expr(children[0])
        else:
            return Expr(children[1])


    def visit_boolean_expression(self,node,children):
        if(len(children) == 1):
            return children[0]
        else:
            if children[1] == "==":
                return (IsEqualTo(children[0],children[2]))
            elif children[1] == "!=":
                return (IsNotEqualTo(children[0],children[2]))
            elif children[1] == ">=":
                return (IsGreaterThanOrEqualTo(children[0],children[2]))
            elif children[1] == ">":
                return (IsGreaterThan(children[0],children[2]))
            elif children[1] == "<=":
                return (IsLessThanOrEqualTo(children[0],children[2]))
            elif children[1] == "<":
                return (IsLessThan(children[0],children[2]))


    def visit_arithmetic_expression(self,node,children):
        if(len(children) == 1):
            return children[0]
        else:
            if children[1] == "+":
                return (Plus(children[0],children[2]))
            elif children[1] == "-":
                return (Minus(children[0],children[2]))

    def visit_mult_term(self,node,children):
        if(len(children) == 1):
            return children[0]
        else:
            if children[1] == "*":
                return (Multiply(children[0],children[2]))
            elif children[1] == "/":
                return (Divide(children[0],children[2]))


    def visit_integer(self,node,children):
        return Integer(int(node.value))

    #NOT YET TESTED
    def visit_function_call(self,node,children):
        if(len(children) == 1 and node[0] == "print"):
            return FunctionCall("print",children[0])
        elif(len(children) == 1):
            return FunctionCall(children[0],CallArguments([]))
        else:
            return FunctionCall(children[0],children[1])


    #NOT YET TESTED
    def visit_call_arguments(self,node,children):
        return CallArguments(children)

    #NOT YET TESTED
    def visit_function_definition(self,node,children):
        return FunctionDefinition(children[0],children[1])

    #NOT YET TESTED
    def visit_param_list(self,node,children):
        return ParamList(children)


    def visit_brace_block(self,node,children):
        return BraceBlock(children[0])
    