from arpeggio import *
from arpeggio import RegExMatch as _
from AstVisitor import *

# general 
def program():   return code, EOF
def code():      return ZeroOrMore(statement)
def statement(): return [("let", variable_declaration), 
                        assignment, 
                        expr]                  


# variable 
def variable_declaration():     return decl, ZeroOrMore(',', decl)
def decl():                     return identifier, Optional("=",expr)
def assignment():               return (identifier, "=", expr)
def variable_reference():       return identifier
def identifier():               return _(r'[a-z][a-zA-Z_0-9]*')

# expression
def expr():                     return [arithmetic_expression]
def primary():                  return [integer, variable_reference, ('(',arithmetic_expression,')')]
def arithmetic_expression():    return  [(multerm, addop, arithmetic_expression),multerm]
def multerm():                  return [(primary, mulop, multerm),primary]

def integer():  return _(r'-?\d+')
def addop():    return ["+", "-"]
def mulop():    return ["*","/"]
def relop():    return  ['==','!=','>=','>','<=','<']


test = """ 
let a = 1
b = 1
1+1
"""
parser = ParserPython(program)
parse_tree = parser.parse(test)
print(parse_tree)
# ast = visit_parse_tree(parse_tree, AstVisitor(debug=False))
# print(ast.evaluate(Binding()))
