from arpeggio import *
from arpeggio import RegExMatch as _
from AstVisitor import *

# general 
def program():   return code, EOF
def code():      return ZeroOrMore(statement)
def statement(): return [("let", variable_declaration), 
                        assignment, 
                        expr]                  

# function
def function_call():        return [(variable_reference,'(',call_arguments,')'),
                                    ("print",'(',call_arguments,')')]
def call_arguments():       return Optional(expr, ZeroOrMore(',',expr))
def function_definitiion(): return (param_list, brace_block)
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
def expr():                     return [("fn",function_definitiion),
                                        arithmetic_expression]
def primary():                  return [integer, function_call, variable_reference, ('(',arithmetic_expression,')')]
def arithmetic_expression():    return  [(multerm, addop, arithmetic_expression),multerm]
def multerm():                  return [(primary, mulop, multerm),primary]

def integer():  return (Optional('-'), _(r'\d+'))
def addop():    return ["+", "-"]
def mulop():    return ["*","/"]
def relop():    return ['==','!=','>=','>','<=','<']


test = """ 
let three = fn (x) {x+3}
three(0)
"""

# let three = fn () {1+2}
# three()

parser = ParserPython(program)
parse_tree = parser.parse(test)
print(parse_tree)
ast = visit_parse_tree(parse_tree, AstVisitor(debug=True))
ast.evaluate(Binding())
