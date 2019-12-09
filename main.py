from arpeggio import ParserPython, PTNodeVisitor, visit_parse_tree
from Grammar import *
from AstVisitor import *

code = "1*2"

parser = ParserPython(expr)
parse_tree = parser.parse(code)
ast = visit_parse_tree(parse_tree, AstVistor(debug=True))
ast.evaluate()

