from grammar import *
from visitor import *


parser = ParserPython(program,comment)
parse_tree = parser.parse("if 3 > 1 {\nprint(99) \n}")

print(parse_tree)

PTDOTExporter().exportFile(parse_tree,"my_parse_tree.dot")

solution = visit_parse_tree(parse_tree, SmurfVisitor(debug=False))

print(solution.evaluate())