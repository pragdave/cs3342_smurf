from arpeggio import *#ZeroOrMore, OneOrMore, Optional, EOF, ParserPython
from arpeggio.export import PMDOTExporter
from arpeggio.export import PTDOTExporter
from arpeggio import RegExMatch as _
    
def program():                  return code, EOF
def comment():                  return _(r'#.*')
def code():                     return ZeroOrMore(statement)                                                                            #done
def statement():                return [("let", variable_declaration), assignment, expr]                                                #done
def variable_declaration():     return decl, ZeroOrMore(",", decl)                                                                      #done
def decl():                     return identifier, Optional("=",expr)                                                                   #done
def identifier():               return _(r'[a-z][a-zA-Z_0-9]*')                                                                         #done
def variable_reference():       return identifier                                                                                       #done
def if_expression():            return expr, brace_block, Optional("else",brace_block)
def assignment():               return identifier, "=", expr                                                                            #done
def expr():                     return [("fn",function_definition),("if",if_expression),boolean_expression,arithmetic_expression]       #done
def boolean_expression():       return arithmetic_expression, relop, arithmetic_expression                                              #done
def arithmetic_expression():    return [(mult_term, addop, arithmetic_expression),mult_term]                                            #done
def mult_term():                return [(primary,mulop,mult_term),primary]                                                              #done
def primary():                  return [integer,function_call,variable_reference,("(",arithmetic_expression,")")]
def integer():                  return _(r'-?[0-9]+')                                                                                   #done
def addop():                    return ["+","-"]                                                                                        #done
def mulop():                    return ["*","/"]                                                                                        #done
def relop():                    return ["==","!=",">=",">","<=","<"]                                                                    #done
def function_call():            return [("print","(",call_arguments,")"),(variable_reference,"(",call_arguments,")")]
def call_arguments():           return Optional(expr, ZeroOrMore(expr))
def function_definition():      return param_list, brace_block
def param_list():               return [("(",identifier,ZeroOrMore(identifier),")"),("(",")")]
def brace_block():              return "{",code,"}"
