from arpeggio import ParserPython
from Grammar import *
from AstVisitor import *


code = """
  -1
"""

parser = ParserPython(arithemtic_expression)
parse_tree = parser.parse(code)
ast = visit_parse_tree(parse_tree, AstVistor(debug=False))
print(ast)

