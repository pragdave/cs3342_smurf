#pip install arpeggio
from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython
import string

aToz = []
for i in string.ascii_lowercase:
    aToz.append(i)
identChars = []
for i in (string.ascii_letters + string.digits + "_"):
    identChars.append(i)

def program(): return               (code, EOF)

def comment(): return               ("#", _(r'.*'))

def code(): return                  ZeroOrMore(statement)

def statement(): return             [("let", variable_declaration), assignment, expr]

def variable_declaration(): return  (decl, ZeroOrMore((",", decl)))

def decl(): return                  (identifier, Optional(("=", expr)))

def identifier(): return            (aToz, ZeroOrMore(identChars))

def variable_reference(): return    identifier

def if_expression(): return         (expr, brace_block, Optional(("else", brace_block)))

def assignment(): return            (identifier, "=", expr)

def expr(): return                  [("fn", function_definition), ("if", if_expression), boolean_expression, arithmetic_expression]

def boolean_expression(): return    (arithmetic_expression, relop, arithmetic_expression)

def arithmetic_expression(): return [(mult_term, addop, arithmetic_expression), mult_term]

def mult_term(): return             [(primary, mulop, mult_term,), primary]

def primary(): return               [_(r'\d'), function_call, variable_reference, ("(", arithmetic_expression, ")")]

def integer(): return               (Optional("-"), OneOrMore(_(r'\d')))

def addop(): return                 ["+", "-"]

def mulop(): return                 ["*", "/"]

def relop(): return                 ["==", "!=", ">=", ">", "<=", "<"]

def function_call(): return         [(variable_reference, "(", call_arguments, ")"), ("print", "(", call_arguments, ")")]

def call_arguments(): return        Optional((expr, ZeroOrMore((",", expr))))

def function_definition(): return   (param_list, brace_block)

def param_list(): return            [("(", identifier, ZeroOrMore((",", identifier)), ")"), ("(",")")]

def brace_block(): return           ("{", code, "}")
'''
def number():     return _(r'\d*\.\d*|\d+')
def factor():     return Optional(["+","-"]), [number, ("(", expression, ")")]
def term():       return factor, ZeroOrMore(["*","/"], factor)
def expression(): return term, ZeroOrMore(["+", "-"], term)
def calc():       return expression, EOF
'''

parser = ParserPython(program, debug=True)   # calc is the root rule of your grammar
                              # Use param debug=True for verbose debugging
                              # messages and grammar and parse tree visualization
                              # using graphviz and dot
                              # add debug=True for thourough print and .dot file
                              # dot -Tpng -O .\program_parse_tree.dot to turn dot to png
parse_tree = parser.parse("(4 - 1) * 5 + (2 + 4) + 7")   

print(parse_tree)     

parse_tree = parser.parse("let x0Z_y = 3")   

print(parse_tree)         

parse_tree = parser.parse("let x, y, z")   

print(parse_tree)   

parse_tree = parser.parse("if 3 <= 4 { let x = 4 } else {let y = 4}")   

print(parse_tree)                               
                            