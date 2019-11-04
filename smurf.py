from arpeggio import *
from arpeggio.export import PMDOTExporter
from arpeggio.export import PTDOTExporter
from arpeggio import RegExMatch as _

def program():                  return code, EOF
def comment():                  return _(r'#.*')
def code():                     return ZeroOrMore(statement)
def statement():                return [("let", variable_declaration),assignment,expr]
def variable_declaration():     return decl, ZeroOrMore(",", decl)
def decl():                     return identifier, Optional("=",expr)
def identifier():               return _(r'[a-z][a-zA-z_0-9]*')
def variable_reference():       return identifier
def if_expression():            return expr, brace_block, Optional("else",brace_block)
def assignment():               return identifier, "=", expr
def expr():                     return [("fn",function_definition),("if",if_expression),boolean_expression,arithmetic_expression]
def boolean_expression():       return arithmetic_expression, relop, arithmetic_expression
def arithmetic_expression():    return [(mult_term,addop,arithmetic_expression),mult_term]
def mult_term():                return [(primary,mulop,mult_term),primary]
def primary():                  return [integer,function_call,variable_reference,("(",arithmetic_expression,")")]
def integer():                  return _(r'-?[0-9]+')
def addop():                    return ["+","-"]
def mulop():                    return ["*","/"]
def relop():                    return ["==","!=",">=",">","<=","<"]
def function_call():            return [(variable_reference,"(",call_arguments,")"),("print","(",call_arguments,")")]
def call_arguments():           return Optional(expr, ZeroOrMore(",",expr))
def function_definition():      return param_list,brace_block
def param_list():               return [("(",identifier, ZeroOrMore(",",identifier),")"),("(",")")]
def brace_block():              return "{",code,"}"

parser = ParserPython(program,comment)
result = parser.parse("#some code")

print(result)
PMDOTExporter().exportFile(parser.parser_model,"PM.dot")
PTDOTExporter().exportFile(result,"PT.dot")