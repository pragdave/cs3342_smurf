from arpeggio.cleanpeg import ParserPEG,visit_parse_tree
from AstVisitor import *

import sys

grammar = """
    expr 
        = arithmetic_expression EOF

    arithmetic_expression
        = multerm addop arithmetic_expression
        / multerm

    multerm
        = primary mulop multerm
        / primary

    primary
        = integer
        / "(" arithmetic_expression ")"

    integer
        = "-"? r'[0-9]+'

    addop
        = '+' / '-'
    mulop
        = '*' / '/'
"""

code = "1--1"

parser = ParserPEG(grammar, "expr", debug=False)
parse_tree = parser.parse(code)
ast = visit_parse_tree(parse_tree, AstVistor(debug=False))
print(ast.accept())

