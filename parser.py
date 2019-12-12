#Dylan Weeks
#alot of the logic and parsing is functional,
#but i had so much trouble when it came to binding and could not figure all the features neede

from arpeggio.cleanpeg import ParserPEG
from arpeggio import ParserPython, PTNodeVisitor, visit_parse_tree 
from ast       import *
from interpreter       import Interpreter
from sys       import argv 

#STYLED GRAMMER OF OF THE EXACT FORMAT FROM THE README
grammer = """
program = code EOF

comment = "#" r'.*'

statement = "let" variable_declaration / assignment / expr

variable_declaration  = decl ("," decl)*

decl = identifier ("=" expr)?

code = statement*

identifier = r'[a-z][a-zA-Z_0-9]*'

variable_reference = identifier

assignment  = identifier "=" expr

expr  = "fn" function_definition / "if" if_expression /boolean_expression / arithmetic_expression

boolean_expression  = arithmetic_expression relop arithmetic_expression

arithmetic_expression  = mult_term addop arithmetic_expression / mult_term

if_expression = expr brace_block ( "else" brace_block )?

mult_term  = primary mulop mult_term / primary

integer = "-"? r'[0-9]+'

addop = '+' / '-'

mulop = '*' / '/'

relop   = '==' / '!=' / '>=' / '>' / '<=' / '<'

primary    = integer / function_call / variable_reference / "(" arithmetic_expression ")"

function_call  = variable_reference "(" call_arguments ")" / "print" "(" call_arguments ")"

call_arguments = (expr ("," expr)*)?

function_definition = param_list brace_block

param_list =  "(" identifier ("," identifier)* ")" / "(" ")"

brace_block = "{" code  "}"
"""
with open(argv[1]) as file:
  filePath = file.read()

#PARSERPG WENT ALONG BEST WITH MY SYTAX FOR THE GRAMMER

#PARSERS THROUGHT THE WHOLE SYTAX
parser = ParserPEG(grammer, "program", "comment")

#THIS IS THE PARSING FOR THE FILE
parse_tree = parser.parse(filePath)

#THIS IS THE BUILDING OF ASTTREE
ast = visit_parse_tree(parse_tree, Visitor())

#CALLS INTERPRETER
ast.accept(Interpreter())
