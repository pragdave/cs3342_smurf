from arpeggio import ParserPython, PTNodeVisitor, visit_parse_tree
from Grammar import *
from AstVisitor import *

code = "a=1"

parser = ParserPython(expr)
parse_tree = parser.parse(code)
print(parse_tree)
# ast = visit_parse_tree(parse_tree, AstVistor(debug=False))
# print(ast.accept())

