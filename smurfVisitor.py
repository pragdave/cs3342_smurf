from smurfGrammar import *
from smurfInterpreter import *

class SmurfVisitor(PTNodeVisitor):

    def visit_program(self,node,children):
        return (Program(children[0]))


    def visit_code(self,node,children):
        return (Code(children))


    def visit_variable_declaration(self,node,children):
        return (Variable_Declaration(children))


    def visit_decl(self,node,children):
        if len(children) == 1:
            return (Decl(children[0],0))
        else:
            return (Decl(children[0],children[1]))


    def visit_identifier(self,node,children):
        return (Identifier(str(node.value)))


    def visit_variable_reference(self,node,children):
        return (Variable_Reference(node.value))


    def visit_if_expression(self,node,children):
        if len(children) == 2:
            return (If_Expression(children[0],children[1]))
        else:
            return (If_Expression(children[0],children[1],children[2]))


    def visit_assignment(self,node,children):
        return (Assignment(children[0],children[1]))


    def visit_boolean_expression(self,node,children):
        if children[1] == "==":
            return (Equal(children[0],children[2]))
        elif children[1] == "!=":
            return (NotEqual(children[0],children[2]))
        elif children[1] == ">=":
            return (GreaterEqual(children[0],children[2]))
        elif children[1] == ">":
            return (Greater(children[0],children[2]))
        elif children[1] == "<=":
            return (LessEqual(children[0],children[2]))
        elif children[1] == "<":
            return (Less(children[0],children[2]))


    def visit_arithmetic_expression(self,node,children):
        if len(children) == 1:
            return children[0]
        else:
            if children[1] == "+":
                return (Plus(children[0],children[2]))
            elif children[1] == "-":
                return (Minus(children[0],children[2]))


    def visit_mult_term(self,node,children):
        if len(children) == 1:
            return children[0]
        else:
            if children[1] == "*":
                return (Times(children[0],children[2]))
            elif children[1] == "/":
                return (Divide(children[0],children[2]))


    def visit_integer(self,node,children):
        return Integer(int(node.value))
        

    def visit_function_call(self,node,children):
        if len(children) == 0:
            return (Function_Call(Call_Arguments([]),"print"))
        elif len(children) == 1 and node[0] == "print":
            return (Function_Call(children[0],"print"))
        elif len(children) == 1:
            return (Function_Call(Call_Arguments([]),children[0]))
        else:
            return (Function_Call(children[1],children[0]))


    def visit_call_arguments(self,node,children):
        return (Call_Arguments(children))


    def visit_function_definition(self,node,children):
        return (Function_Definition(children[0],children[1]))


    def visit_param_list(self,node,children):
        return (Param_List(children))