from arpeggio import *
from arpeggio import RegExMatch as _
from AstVisitor import *

# general 
def program():   return code,EOF
def comment():   return '#',_(r'.*')
def code():      return ZeroOrMore(statement)
def statement(): return [("let", variable_declaration), 
                        assignment, 
                        expr]                  

# function
def function_call():        return [(variable_reference,'(',call_arguments,')'),
                                    ("print",'(',call_arguments,')')]
def call_arguments():       return Optional(expr, ZeroOrMore(',',expr))
def function_definition(): return (param_list, brace_block)
def param_list():           return [('(',identifier, ZeroOrMore(',',identifier),')'),
                                    ('(',')')]
def brace_block():          return ('{',code,'}')

# variable 
def variable_declaration():     return decl, ZeroOrMore(',', decl)
def decl():                     return identifier, Optional("=",expr)
def assignment():               return (identifier, "=", expr)
def variable_reference():       return identifier
def identifier():               return _(r'[a-z][a-zA-Z_0-9]*')

# expression
def expr():                     return  [("fn",function_definition),
                                         ("if",if_expression),
                                         boolean_expression,
                                         arithmetic_expression]
def primary():                  return  [integer, function_call, variable_reference, ('(',arithmetic_expression,')')]
def arithmetic_expression():    return  [(multerm, addop, arithmetic_expression),multerm]
def multerm():                  return  [(primary, mulop, multerm),primary]
def if_expression():            return  (expr,brace_block, Optional("else", brace_block))
def boolean_expression():      return   (arithmetic_expression,relop,arithmetic_expression)

def integer():  return (Optional('-'), _(r'\d+'))
def addop():    return ["+", "-"]
def mulop():    return ["*","/"]
def relop():    return ['==','!=','>=','>','<=','<']

def run(test):
    parser = ParserPython(program,comment)
    parse_tree = parser.parse(test)
    ast = visit_parse_tree(parse_tree, AstVisitor(debug=False))
    ast.evaluate(Binding())
