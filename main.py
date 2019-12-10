from arpeggio import ParserPython, PTNodeVisitor, visit_parse_tree
from Grammar import *
from AstVisitor import *

code = "(3-1)*(3+1)"

parser = ParserPython(expr)
parse_tree = parser.parse(code)
ast = visit_parse_tree(parse_tree, AstVistor(debug=False))
print(ast.accept())

