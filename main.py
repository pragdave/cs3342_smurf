from grammar import *
from visitor import *


parser = ParserPython(program,comment)
parse_tree = parser.parse("let a = 4, b = 5, c = 6")

print(parse_tree)

PTDOTExporter().exportFile(parse_tree,"my_parse_tree.dot")

solution = visit_parse_tree(parse_tree, SmurfVisitor(debug=False))

print(solution.evaluate())