from arpeggio import *
from arpeggio import RegExMatch as _

def start():                    return OneOrMore(assignment), EOF
def assignment():               return identifier, "=", expr
def variable_reference():       return identifier
def identifier():                return _(r'[a-z][a-zA-Z_0-9]*')

def expr():                     return [arithmetic_expression]
def primary():                  return [integer, variable_reference, ('(',arithmetic_expression,')')]

def arithmetic_expression():    return  [(multerm, addop, arithmetic_expression),multerm]
def multerm():                  return [(primary, mulop, multerm),primary]

def integer():  return _(r'-?\d+')
def addop():    return ["+", "-"]
def mulop():    return ["*","/"]
def relop():    return  ['==','!=','>=','>','<=','<']


code = "a = 1"
parser = ParserPython(start)
parse_tree = parser.parse(code)
print(parse_tree)