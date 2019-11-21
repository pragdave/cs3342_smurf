from smurfGrammar import *
from smurfVisitor import *
import sys

parser = ParserPython(program,comment)

f = sys.argv[1]
print()
file = open(f,"r")
contents = file.read()

parseTree = parser.parse(contents)
myAST = visit_parse_tree(parseTree,SmurfVisitor(debug=False))
myAST.evaluate()