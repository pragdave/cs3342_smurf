
from arpeggio.cleanpeg import ParserPEG, visit_parse_tree

import sys
from sys import argv, path

sys.path.append("c:/Users/hawx5/OneDrive - Southern Methodist University/CS 3342/cs3342_smurf/src/")

from ast_generator import VisitorClass
from interpreter import *

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
  = r'[a-z][a-zA-Z_0-9]*'

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
  / "print" "(" call_arguments ")"

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

def runGrammar(program):
  parser = ParserPEG(grammar, "program", "comment", debug=False)
  tree = parser.parse(program)
  ast = visit_parse_tree(tree, VisitorClass(debug=True))
  ast.accept(Interpreter())

# runGrammar("""
# let a = 99
# let f = fn(x) { x + a }

# print(f(1))     #=> 100

# # check it's a live reference
# a = 100
# print(f(1))     #=> 101

# # check function execution creates a closure

# let add_n = fn (n) { fn (x) { x + n }}
# let add_2 = add_n(2)
# let add_3 = add_n(3)
# print(add_2(2))       #=> 4
# print(add_3(10))      #=> 13
# print(add_3(2))       #=> 5
# print(add_2(10))      #=> 12
# """)