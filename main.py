from arpeggio import ParserPython
from test_grammar import *


code = """
  1+1
"""

parser = ParserPython(arithemtic_expression)
parse_tree = parser.parse(code)
print(parse_tree)
