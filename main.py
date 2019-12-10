from grammar import *
from visitor import *


parser = ParserPython(program,comment)

f = sys.argv[1]
print()
file = open(f,"r")
contents = file.read()

parse_tree = parser.parse(contents)
PTDOTExporter().exportFile(parse_tree,"my_parse_tree.dot")
solution = visit_parse_tree(parse_tree, SmurfVisitor(debug=False))
solution.evaluate()
