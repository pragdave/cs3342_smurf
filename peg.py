from arpeggio.cleanpeg import ParserPEG,visit_parse_tree
from AstVisitor import *

import sys

grammar = """
    start 
        = assignment* EOF
   
    assignment 
        = identifier "=" expr

    expr 
        = arithmetic_expression

    arithmetic_expression
        = multerm addop arithmetic_expression
        / multerm

    multerm
        = primary mulop multerm
        / primary

    primary
        = integer
        / variable_value
        / "(" arithmetic_expression ")"

    variable_value = 
        identifier

    identifier 
        = r'[a-z][a-zA-Z_0-9]*'

    integer
        = "-"? r'[0-9]+'

    addop
        = '+' / '-'
    mulop
        = '*' / '/'
"""

code = "a=3"

parser = ParserPEG(grammar, "start", debug=True)
parse_tree = parser.parse(code)
print(parse_tree)
# ast = visit_parse_tree(parse_tree, AstVistor(debug=False))
# print(ast.accept())

