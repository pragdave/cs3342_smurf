from arpeggio import *
from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython
import os


def program(): return code, EOF

def comment(): return "#", _(r'.*')

def code() : return ZeroOrMore(statement)

def statement() : return [("let", variable_declaration) , assignment , expr]
          
def variable_declaration(): return decl, ZeroOrMore(",", decl)

def decl(): return identifier, Optional("=", expr)

def identifier() : return [_(r'[a-z]')], ZeroOrMore([_(r'\w+')])

def variable_reference(): return identifier

def if_expression(): return expr, brace_block, Optional( "else", brace_block )

def assignment(): return identifier, "=", expr

def expr(): return [("fn", function_definition), ("if", if_expression) , boolean_expression ,arithmetic_expression]

def boolean_expression(): return arithmetic_expression, relop, arithmetic_expression

def arithmetic_expression(): return [(mult_term, addop, arithmetic_expression) , mult_term]

def mult_term(): return [(primary, mulop, mult_term) , primary]

def primary():  return [integer , function_call , variable_reference , ( "(", arithmetic_expression, ")")]


def integer(): return Optional("-"), OneOrMore(_(r'\d+'))
#def integer(): return Optional("-"), OneOrMore(_(r'[0-9]'))

def addop(): return ['+',  '-']
def mulop(): return ['*' , '/']
def relop(): return ['==' , '!=' , '>=' , '>' , '<=' , '<']


def function_call(): return [(variable_reference, "(", call_arguments, ")") , ("print", "(", call_arguments, ")")]

def call_arguments(): return Optional(expr, ZeroOrMore(",", expr))

def function_definition(): return param_list, brace_block

def param_list():  return [("(", identifier, ZeroOrMore(",", identifier), ")") ,  "(" ")"]

def brace_block(): return "{", code, "}"

def main(debug = False):
    #current_dir = os.path.dirname(__file__)
    #test_program = open(os.path.join(current_dir, 'C:\\Users\\mailt\Documents\\GitHub\\cs3342_smurf\\test_cases\\00_expr.smu')).read()
    parser = ParserPython(program, comment, debug = debug)
    #parse_tree = parser_parse(test_program)
    parser_tree = parser.parse("1 + (2 * 3)")
    print(parser_tree)

if __name__ == "__main__":
    main(debug=True)
