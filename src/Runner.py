from arpeggio.cleanpeg import ParserPEG, visit_parse_tree

import sys
from sys import argv, path
from Interpreter import *
from Visitor import *


grammar = """
program 
  = code EOF
comment 
  = "#" r'.*'
code 
  = statement*
statement 
  = "let" variable_decl
  / assignment
  / expr
variable_decl
  = decl ("," decl)*
decl 
  = identifier ("=" expr)?
identifier 
  = r'[a-zA-Z_][a-zA-Z0-9_]*'
variable_reference 
  = identifier
if_expr 
  = expr brace_block ( "else" brace_block )?
assignment  
  = identifier "=" expr
expr 
  = "fn" function_def
  / "if" if_expr
  / boolean_expr
  / arithmetic_expr
boolean_expr 
  = arithmetic_expr relop arithmetic_expr 
arithmetic_expr  
  = mult_term addop arithmetic_expr
  / mult_term
mult_term 
  = primary mulop mult_term
  / primary
primary 
  = integer
  / print_call
  / function_call
  / variable_reference
  / "(" arithmetic_expr ")"
integer 
  = "-"? r'[0-9]+'
addop 
  = '+' / '-'
mulop 
  = '*' / '/'
relop 
  = '==' / '!=' / '>=' / '>' / '<=' / '<'
function_call 
  = variable_reference "(" call_arguments ")"
print_call
  = "print" "(" call_arguments ")"
call_arguments 
  = (expr ("," expr)*)?
function_def 
  = param_list brace_block
param_list 
  = "(" identifier ("," identifier)* ")"
  /  "(" ")"
brace_block 
  = "{" code  "}"
"""
def run(program):
    parser = ParserPEG(grammar, "program", "comment", debug=False)
    tree = parser.parse(program)
    ast = visit_parse_tree(tree, VisitorClass(debug=False))
    ast.eval(Interpreter())

with open(argv[1]) as file:
    contents = file.read()
run(contents)