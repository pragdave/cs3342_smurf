from arpeggio.cleanpeg import ParserPEG
import sys

grammar = """
    arithmentic_expression
        = mult_term (addop mult_term)*
    mult_term
        = primary (mulop primary)*
    primary
        = integer
        / "(" arithmentic_expression ")"
    integer
        = "-"? r'[0-9]+'
    addop
        = '+' / '-'
    mulop
        = '*' / '/'
"""
parser = ParserPEG(grammar, "arithmentic_expression", debug=True)
tree = parser.parse(sys.argv[1])